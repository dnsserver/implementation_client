from setuptools import setup, find_packages

setup(
        name='opal_client',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'flask',
            'flask_sqlalchemy',
            'flask_admin',
            'flask_oidc',
            'flask_bootstrap',
            'flask_nav',
        ],
        setup_requires=[
            'pytest-runner',
        ],
        tests_require=[
            'pytest',
        ]
)
