import textwrap

import setuptools

version = "1.0"


if __name__ == "__main__":
    setuptools.setup(
        name="pygitee",
        version=version,
        description="Use the full gitee API v5",
        author="kingreatwill",
        author_email="kingreatwill@qq.com",
        url="https://gitee.com/kingreatwill/pygitee",
        long_description=textwrap.dedent(
            """\
            (Very short) Tutorial
            =====================
            First create a Github instance::
                from github import Github
                # using username and password
                g = Github("user", "password")
                # or using an access token
                g = Github("access_token")
            Then play with your Github objects::
                for repo in g.get_user().get_repos():
                    print(repo.name)
                    repo.edit(has_wiki=False)
            Reference documentation
            =======================
            See https://gitee.com/kingreatwill/pygitee/"""
        ),
        packages=["gitee"],
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development",
        ],
        python_requires=">=3.5",
        install_requires=["deprecated", "pyjwt", "requests>=2.24.0"],
        extras_require={"integrations": ["cryptography"]},
        tests_require=["cryptography", "httpretty>=0.9.6"],
    )