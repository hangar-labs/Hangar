from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AdminContact(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="admin_contact")
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    city: Optional[str] = None
    contact_type: Optional[str] = None
    country_code: Optional[str] = None
    email: Optional[str] = None
    extra_params: Optional[Dict[str, str]] = None
    fax: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization_name: Optional[str] = None
    phone_number: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


@define(kw_only=True, slots=False)
class NameServer(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="name_server")
    glue_ips: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class RegistrantContact(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="registrant_contact")
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    city: Optional[str] = None
    contact_type: Optional[str] = None
    country_code: Optional[str] = None
    email: Optional[str] = None
    extra_params: Optional[Dict[str, str]] = None
    fax: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization_name: Optional[str] = None
    phone_number: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


@define(kw_only=True, slots=False)
class TechContact(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tech_contact")
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    city: Optional[str] = None
    contact_type: Optional[str] = None
    country_code: Optional[str] = None
    email: Optional[str] = None
    extra_params: Optional[Dict[str, str]] = None
    fax: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization_name: Optional[str] = None
    phone_number: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53domainsRegisteredDomain(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53domains_registered_domain")
    admin_contact: Optional[Sequence[AdminContact]] = None
    admin_privacy: Optional[bool] = None
    auto_renew: Optional[bool] = None
    name_server: Optional[Sequence[NameServer]] = None
    registrant_contact: Optional[Sequence[RegistrantContact]] = None
    registrant_privacy: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tech_contact: Optional[Sequence[TechContact]] = None
    tech_privacy: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
    transfer_lock: Optional[bool] = None
