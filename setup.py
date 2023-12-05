from setuptools import setup

setup(
    name='cypyapi',
    version='1.0.0',
    description='cloud.gov API',
    author='Ephraim',
    packages=['Santas bag'],
    install_requires=[
        'aiohttp'==3.8.4,
        'aiosignal'==1.3.1,
        'apispec'==6.0.2,
        'async-timeout'==4.0.2,
        'attrs'==22.2.0,
        'awscli-local'==0.20,
        'blinker'==1.7.0,
        'boto3'==1.24.96,
        'botocore'==1.27.96,
        'cachetools'==5.0.0,
        'certifi'==2022.9.24,
        'cffi'==1.15.1,
        'charset-normalizer'==2.1.1,
        'click'==8.1.3,
        'commonmark'==0.9.1,
        'cryptography'==38.0.4,
        'dataclasses-json'==0.5.7,
        'dill'==0.3.2,
        'dnslib'==0.9.23,
        'dnspython'==2.2.1,
        'ecdsa'==0.18.0,
        'Flask'==3.0.0,
        'frozenlist'==1.3.3,
        'greenlet'==2.0.2,
        'idna'==3.4,
        'itsdangerous'==2.1.2,
        'Jinja2'==3.1.2,
        'jmespath'==1.0.1,
        'langchain'==0.0.157,
        'llama-index'==0.6.5,
        'localstack'==1.3.0,
        'localstack-client'==1.39,
        'localstack-ext'==1.3.0,
        'MarkupSafe'==2.1.3,
        'marshmallow'==3.19.0,
        'marshmallow-enum'==1.5.1,
        'multidict'==6.0.4,
        'mypy-extensions'==1.0.0,
        'newrelic-telemetry-sdk'==0.4.3,
        'nr-openai-observability'==0.2.4,
        'numexpr'==2.8.4,
        'numpy'==1.24.3,
        'openai'==0.27.2,
        'openapi-schema-pydantic'==1.2.4,
        'packaging'==21.3,
        'pandas'==2.0.1,
        'pbr'==5.11.0,
        'pip'==23.1.2,
        'plux'==1.3.1,
        'psutil'==5.9.4,
        'pyaes'==1.6.1,
        'pyasn1'==0.4.8,
        'pycparser'==2.21,
        'pydantic'==1.10.7,
        'Pygments'==2.13.0,
        'pyparsing'==3.0.9,
        'python-dateutil'==2.8.2,
        'python-dotenv'==0.21.0,
        'python-jose'==3.3.0,
        'pytz'==2023.3,
        'PyYAML'==6.0,
        'regex'==2023.5.4,
        'requests'==2.28.1,
        'rich'==12.6.0,
        'rsa'==4.9,
        's3transfer'==0.6.0,
        'semver'==2.13.0,
        'setuptools'==63.2.0,
        'six'==1.16.0,
        'SQLAlchemy'==2.0.12,
        'stevedore'==4.1.1,
        'tabulate'==0.9.0,
        'tailer'==0.4.1,
        'tenacity'==8.2.2,
        'tiktoken'==0.3.3,
        'tqdm'==4.65.0,
        'typing_extensions'==4.5.0,
        'typing-inspect'==0.8.0,
        'tzdata'==2023.3,
        'urllib3'==1.26.13,
        'Werkzeug'==3.0.1,
        'yarl'==1.8.2,
    ],
)