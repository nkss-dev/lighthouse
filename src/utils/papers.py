import re
import subprocess
from base64 import b64decode
from typing import Literal, NamedTuple
import requests


class NixPaper(NamedTuple):
    code: str
    exam: Literal["ms1", "ms2", "ms3", "es"]
    year: int

    contents: str

    @staticmethod
    def load_contents(contents_url):
        with requests.get(contents_url) as response:
            if response.ok:
                contents_nix = b64decode(response.json()["content"]).decode()
                try:
                    result = subprocess.run(
                        ["nix", "eval", "--json", "--expr", "'{ x = 1; }'"],
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    return result.stdout.strip()
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
                    raise
            else:
                raise Exception


async def fetch_papers(**kwargs):
    paper_pattern = r"\w{6,7}-(ms1|ms2|ms3|es)-\d{4}(-\w{3})?\.nix"
    with requests.get(
        "https://api.github.com/repos/nkss-dev/atlas/contents/question-papers"
    ) as response:
        if response.ok:
            papers = []
            for paper in response.json():
                if re.fullmatch(paper_pattern, paper["name"]):
                    name, _ = paper["name"].split(".")
                    code, exam, year = name.split("-")
                    papers.append(
                        NixPaper(
                            code, exam, year, NixPaper.load_contents(paper["git_url"])
                        )
                    )
                    break
        else:
            raise Exception
    return papers
