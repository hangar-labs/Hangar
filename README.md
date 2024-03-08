# Hangar

## Modern infrastructure-as-code

Hangar is a tool that allows you to provision, interact with, and orchestrate your infrastructure.

```python
@app.Function( timeout=60 * 2, environment_variables={"test": "test"})
def hangarfunction(description):
    return os.getenv("test")

func.invoke(payload={"key": "value"}) == "Hello, world!"
```

Hangar currently supports the following basic services on AWS:
- S3
- EC2
- Lambda
- VPC

### Install

'pip install hangar-sdk'

### Roadmap
- [ ] ECS Support
- [ ] Edge function support (AWS, Cloudflare)
- [ ] Function import + requirements auto generation
- [ ] GCP Support
- [ ] Azure GPU support
- [ ] Serverless GPU Cloud
- [ ] Automatic replay

### Known Bugs
- When testing, lambda package files are not automatically destroyed


## We are still figuring this out. If you have suggestions, please open an issue and a core team member will respond.

## Attribution

This repository contains code from [chalice](https://github.com/aws/chalice). It is used in for cross platform building of packages.