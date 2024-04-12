import re
from modules import util
from modules.util import Failed

logger = util.logger

raw_url = "https://raw.githubusercontent.com"
base_url = "https://api.github.com"
kometa_base = f"{base_url}/repos/meisnate12/Kometa"
configs_raw_url = f"{raw_url}/kometa-team/Kometa-Configs"

class GitHub:
    def __init__(self, config, params):
        self.config = config
        self.token = params["token"]
        logger.secret(self.token)
        self.headers = {"Authorization": f"token {self.token}"} if self.token else None
        self.images_raw_url = f"{raw_url}/meisnate12/PMM-Image-Sets/master/sets/"
        self.translation_url = f"{raw_url}/kometa-team/Kometa-Translations/master/defaults/"
        self._configs_url = None
        self._config_tags = []
        self._translation_keys = []
        self._translations = {}

    def _requests(self, url, err_msg=None, json=True, params=None):
        response = self.config.get(url, headers=self.headers, params=params)
        if not err_msg:
            err_msg = f"URL Not Found: {url}"
        if response.status_code >= 400:
            raise Failed(f"Git Error: {err_msg}")
        if json:
            try:
                return response.json()
            except ValueError:
                logger.error(str(response.content))
                raise
        return response

    def get_top_tree(self, repo):
        if not str(repo).startswith("/"):
            repo = f"/{repo}"
        if not str(repo).endswith("/"):
            repo = f"{repo}/"
        data = self._requests(f"{base_url}/repos{repo}commits", f"No repo found at https://github.com{repo}")
        return self.get_tree(data[0]["commit"]["tree"]["url"]), repo

    def get_tree(self, tree_url):
        return {i["path"]: i for i in self._requests(tree_url, f"No tree found at {tree_url}")["tree"]}

    def latest_release_notes(self):
        return self._requests(f"{kometa_base}/releases/latest")["body"]

    def get_commits(self, dev_version, nightly=False):
        master_sha = self._requests(f"{kometa_base}/commits/master")["sha"]
        response = self._requests(f"{kometa_base}/commits", params={"sha": "nightly" if nightly else "develop"})
        commits = []
        for commit in response:
            if commit["sha"] == master_sha:
                break
            message = commit["commit"]["message"]
            match = re.match(r"^\[(\d)]", message)
            if match and int(match.group(1)) <= dev_version:
                break
            commits.append(message)
        return "\n".join(commits)

    @property
    def config_tags(self):
        if not self._config_tags:
            try:
                self._config_tags = [r["ref"][11:] for r in self._requests(f"{kometa_base}-Configs/git/refs/tags")]
            except TypeError:
                pass
        return self._config_tags

    @property
    def configs_url(self):
        if self._configs_url is None:
            self._configs_url = f"{configs_raw_url}/master/"
            if self.config.version[1] in self.config_tags and (self.config.latest_version[1] != self.config.version[1] or self.config.branch == "master"):
                self._configs_url = f"{configs_raw_url}/v{self.config.version[1]}/"
        return self._configs_url

    @property
    def translation_keys(self):
        if not self._translation_keys:
            tree, repo = self.get_top_tree("kometa-team/Kometa-Translations")
            self._translation_keys = [tk[:-4] for tk in self.get_tree(tree["defaults"]["url"])]
        return self._translation_keys

    def translation_yaml(self, translation_key):
        if translation_key not in self._translations:
            url = f"{self.translation_url}{translation_key}.yml"
            yaml = util.YAML(input_data=self._requests(url, json=False).content).data
            output = {"collections": {}, "key_names": {}, "variables": {}}
            for k in output:
                if k in yaml:
                    output[k] = yaml[k]
            self._translations[translation_key] = output
        return self._translations[translation_key]
