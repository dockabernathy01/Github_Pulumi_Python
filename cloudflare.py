import pulumi
import pulumi_cloudflare as cloudflare

# Define your domain name for which the rule will apply
domain_name = "yourdomain.com"

# Retrieve the Cloudflare zone for the given domain
zone = cloudflare.Zone.get("zone", name=domain_name)

# Create a page rule that forwards the index page to another URL within the same zone
page_rule = cloudflare.PageRule("index-forward",
                                zone_id=zone.id,
                                targets=[cloudflare.PageRuleTargetArgs(
                                    target="url",
                                    constraint=cloudflare.PageRuleTargetConstraintArgs(
                                        operator="matches",
                                        value=f"{domain_name}/index.html"
                                    )
                                )],
                                actions=[cloudflare.PageRuleActionArgs(
                                    type="forwarding_url",
                                    value=cloudflare.PageRuleActionForwardingUrlArgs(
                                        url="https://www.anotherdomain.com/newpage",
                                        status_code=301
                                    )
                                )],
                                priority=1,
                                status="active")

# Export the page rule ID
pulumi.export('page_rule_id', page_rule.id)