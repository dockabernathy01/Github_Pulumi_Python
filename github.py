"""A GitHub Python Pulumi program"""

import pulumi
import pulumi_github as github
# import pulumi_cloudflare as cloudflare

cloudflare_account_id = "f114873b6774d08c95e583a36136d9e3"
project_name = "NewProject"
production_branch = "main"
my_api_key = "YmnKHzXyN9geQc5cENlt2iQUnf7eqtjBCTAlmm-r"
domain_name = "newspaper.com"
# cloudflare_provider = cloudflare.Provider('cloudflare-provider', api_token=my_api_key)

# Create a GitHub repository
# repository = github.Repository('demo-repo', description="Demo Repository for GitHub")

domains = [
    'example-domain-1.com',
    'example-domain-2.com',
    'example-domain-3.com'
]

def create_repositoy_with_domain(domain):
    return github.Repository(domain,
        name=domain,
        description="A new repository from a landing template",
        visibility="private",
        template=github.RepositoryTemplateArgs(
            owner="MOONSTAR0515",
            repository="landing_template"
        )) 

repos = []
for domain in domains:
    # Extract a valid GitHub repo name from the domain by removing special characters
    repo_name = domain.replace('.', '-')
    
    # Create a GitHub repository for each domain
    repo = create_repositoy_with_domain(domain)
    repos.append(repo)

# Export the repository names and URLs
for i, repo in enumerate(repos):
    pulumi.export(f'github_repository_{i+1}_name', repo.name)
    pulumi.export(f'github_repository_{i+1}_html_url', repo.html_url)
