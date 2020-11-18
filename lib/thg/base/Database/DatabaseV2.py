import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///teste_thg", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class ApIkeys(Base):
    """
    tabela referente a criação rest api do thg
    """

    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True)
    token = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"User {self.token}"


class AsyncCallbacks(Base):
    __tablename__ = "async_callbacks"
    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    timestamp = Column(Integer)
    listener_uri = Column(String)
    target_host = Column(String)
    target_port = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class AutomaticExploitationMatchResults(Base):
    __tablename__ = "AutomaticExploitationMatchResults"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer)
    trun_id = Column(Integer)
    state = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["match_id"], name: "index_automatic_exploitation_match_results_on_match_id"
    # t.index ["run_id"], name: "index_automatic_exploitation_match_results_on_run_id"


class AutomaticExploitationMatchSets(Base):
    __tablename__ = "AutomaticExploitationMatchSets"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(String)
    user_id = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["user_id"], name: "index_automatic_exploitation_match_sets_on_user_id"
    # t.index ["workspace_id"], name: "index_automatic_exploitation_match_sets_on_workspace_id"


class AutomaticExploitationMatches(Base):
    __tablename__ = "AutomaticExploitationMatches"
    id = Column(Integer, primary_key=True)
    module_detail_id = Column(Integer)
    state = Column(String)
    nexpose_data_vulnerability_definition_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    match_set_id = Column(Integer)
    matchable_type = Column(String)
    matchable_id = Column(Integer)
    module_fullname = Column(String)
    # t.index ["module_detail_id"], name: "index_automatic_exploitation_matches_on_module_detail_id"
    # t.index ["module_fullname"], name: "index_automatic_exploitation_matches_on_module_fullname"


class AutomaticExploitationRuns(Base):
    __tablename__ = "AutomaticExploitationRuns"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    user_id = Column(Integer)
    match_set_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["match_set_id"], name: "index_automatic_exploitation_runs_on_match_set_id"
    # t.index ["user_id"], name: "index_automatic_exploitation_runs_on_user_id"
    # t.index ["workspace_id"], name: "index_automatic_exploitation_runs_on_workspace_id"


class Clients(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    ua_string = Column(String)
    ua_name = Column(String)
    ua_ver = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class CredentialCoresTasks(Base):
    __tablename__ = "CredentialCoresTasks"
    id = Column(Integer, primary_key=True)
    core_id = Column(Integer)
    task_id = Column(Integer)


class CredentialLoginsTasks(Base):
    __tablename__ = "CredentialLoginsTasks"
    id = Column(Integer, primary_key=True)
    login_id = Column(Integer)
    task_id = Column(Integer)


class Creds(Base):
    __tablename__ = "Creds"
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    service_id = Column(String)
    passwpassw = Column(String)
    active = Column(Boolean, unique=False, default=True)
    active = Column(Boolean, unique=False, default=True)
    proof = Column(String)
    ptype = Column(String)
    source_id = Column(Integer)
    source_type = Column(String)


class Events(Base):
    __tablename__ = "Events"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    host_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    name = Column(String)
    updated_at = Column(DateTime)
    critical = Column(Boolean, unique=False, default=True)
    seen = Column(Boolean, unique=False, default=True)
    username = Column(String)
    info = Column(String)


class ExploitAttempts(Base):
    __tablename__ = "ExploitAttempts"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    service_id = Column(Integer)
    vuln_id = Column(Integer)
    attempted_at = Column(DateTime, default=datetime.datetime.utcnow)
    exploited = Column(Boolean, unique=False, default=True)
    fail_reason = Column(String)
    username = Column(String)
    module = Column(String)
    session_id = Column(Integer)
    loot_id = Column(Integer)
    port = Column(Integer)
    proto = Column(String)
    fail_detail = Column(String)


class ExploitedHosts(Base):
    __tablename__ = "ExploitedHosts"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    service_id = Column(Integer)
    session_uuid = Column(String)
    name = Column(String)
    payload = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class HostDetails(Base):
    __tablename__ = "HostDetails"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    nx_console_id = Column(Integer)
    nx_device_id = Column(Integer)
    src = Column(String)
    nx_site_name = Column(String)
    nx_site_importance = Column(String)
    nx_scan_template = Column(String)
    nx_risk_score = Column(Float)


class Hosts(Base):
    __tablename__ = "Hosts"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    address = Column(String)
    mac = Column(String)
    comm = Column(String)
    name = Column(String)
    state = Column(String)
    os_name = Column(String)
    os_flavor = Column(String)
    os_sp = Column(String)
    os_lang = Column(String)
    arch = Column(String)
    workspace_id = Column(Integer)
    updated_at = Column(DateTime)
    purpose = Column(String)
    info = Column(String)
    comments = Column(String)
    scope = Column(String)
    virtual_host = Column(String)
    note_count = Column(Integer)
    vuln_count = Column(Integer)
    service_count = Column(Integer)
    host_detail_count = Column(Integer)
    exploit_attempt_count = Column(Integer)
    cred_count = Column(Integer)
    detected_arch = Column(String)
    os_family = Column(String)
    # t.index ["name"], name: "index_hosts_on_name"
    # t.index ["os_flavor"], name: "index_hosts_on_os_flavor"
    # t.index ["os_name"], name: "index_hosts_on_os_name"
    # t.index ["purpose"], name: "index_hosts_on_purpose"
    # t.index ["state"], name: "index_hosts_on_state"
    # t.index ["workspace_id", "address"], name: "index_hosts_on_workspace_id_and_address", unique: true


class HostsTags(Base):
    __tablename__ = "HostsTags"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    tag_id = Column(Integer)


class Listeners(Base):
    __tablename__ = "Listeners"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    workspace_id = Column(Integer)
    task_id = Column(Integer)
    enabled = Column(Boolean, unique=False, default=True)
    owner = Column(String)
    payload = Column(String)
    address = Column(String)
    port = Column(Integer)
    options = Column(String)
    macro = Column(String)


class Loots(Base):
    __tablename__ = "Loots"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    host_id = Column(Integer)
    service_id = Column(Integer)
    ltype = Column(String)
    path = Column(String)
    data = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    content_type = Column(String)
    name = Column(String)
    info = Column(String)
    module_run_id = Column(Integer)
    # t.index ["module_run_id"], name: "index_loots_on_module_run_id"


class Macros(Base):
    __tablename__ = "Macros"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    owner = Column(String)
    name = Column(String)
    description = Column(String)
    actions = Column(String)
    prefs = Column(String)


class THGCredentialCores(Base):
    __tablename__ = "THGCredentialCores"
    id = Column(Integer, primary_key=True)
    origin_type = Column(String)
    origin_id = Column(Integer)
    private_id = Column(Integer)
    public_id = Column(Integer)
    realm_id = Column(Integer)
    workspace_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    logins_count = Column(Integer)
    # t.index ["origin_type", "origin_id"], name: "index_THG_credential_cores_on_origin_type_and_origin_id"
    # t.index ["private_id"], name: "index_THG_credential_cores_on_private_id"
    # t.index ["public_id"], name: "index_THG_credential_cores_on_public_id"
    # t.index ["realm_id"], name: "index_THG_credential_cores_on_realm_id"
    # t.index ["workspace_id", "private_id"], name: "unique_private_THG_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NULL) AND (private_id IS NOT NULL))"
    # t.index ["workspace_id", "public_id", "private_id"], name: "unique_realmless_THG_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NOT NULL) AND (private_id IS NOT NULL))"
    # t.index ["workspace_id", "public_id"], name: "unique_public_THG_credential_cores", unique: true, where: "((realm_id IS NULL) AND (public_id IS NOT NULL) AND (private_id IS NULL))"
    # t.index ["workspace_id", "realm_id", "private_id"], name: "unique_publicless_THG_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NULL) AND (private_id IS NOT NULL))"
    # t.index ["workspace_id", "realm_id", "public_id", "private_id"], name: "unique_complete_THG_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NOT NULL) AND (private_id IS NOT NULL))"
    # t.index ["workspace_id", "realm_id", "public_id"], name: "unique_privateless_THG_credential_cores", unique: true, where: "((realm_id IS NOT NULL) AND (public_id IS NOT NULL) AND (private_id IS NULL))"
    # t.index ["workspace_id"], name: "index_THG_credential_cores_on_workspace_id"


class THGCredentialLogins(Base):
    __tablename__ = "THGCredentialLogins"
    id = Column(Integer, primary_key=True)
    core_id = Column(Integer)
    service_id = Column(Integer)
    access_level = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["core_id", "service_id"], name: "index_THG_credential_logins_on_core_id_and_service_id", unique: true
    # t.index ["service_id", "core_id"], name: "index_THG_credential_logins_on_service_id_and_core_id", unique: true


class THGCredentialOriginCrackedPasswords(Base):
    __tablename__ = "THGCredentialOriginCrackedPasswords"
    id = Column(Integer, primary_key=True)
    THG_credential_core_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["THG_credential_core_id"], name:originating_credential_cores


class THGCredentialOriginImports(Base):
    __tablename__ = "THGCredentialOriginImports"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    task_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["task_id"], name: "index_THG_credential_origin_imports_on_task_id"


class THGCredentialOriginManuals(Base):
    __tablename__ = "THGCredentialOriginManuals"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["user_id"], name: "index_THG_credential_origin_manuals_on_user_id"


class THGCredentialOriginServices(Base):
    __tablename__ = "THGCredentialOriginServices"
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    module_full_name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["service_id", "module_full_name"], name: "unique_THG_credential_origin_services", unique: true


class THGCredentialOriginSessions(Base):
    __tablename__ = "THGCredentialOriginSessions"
    id = Column(Integer, primary_key=True)
    post_reference_name = Column(String)
    session_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["session_id", "post_reference_name"], name: "unique_THG_credential_origin_sessions", unique: true


class THGCredentialPrivates(Base):
    __tablename__ = "THGCredentialPrivates"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    data = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    jtr_format = Column(String)
    # t.index "type, decode(md5(data), 'hex'::text)", name: "index_THG_credential_privates_on_type_and_data_sshkey", unique: true, where: "((type)::text = 'lib::Credential::SSHKey'::text)"
    # t.index ["type", "data"], name: "index_THG_credential_privates_on_type_and_data", unique: true, where: "(NOT ((type)::text = 'lib::Credential::SSHKey'::text))"


class THGCredentialPublics(Base):
    __tablename__ = "THGCredentialPublics"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    type = Column(String)
    # t.index ["username"], name: "index_THG_credential_publics_on_username", unique: true


class THGCredentialRealms(Base):
    __tablename__ = "THGCredentialRealms"
    id = Column(Integer, primary_key=True)
    key = Column(String)
    value = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["key", "value"], name: "index_THG_credential_realms_on_key_and_value", unique: true


class ModRefs(Base):
    __tablename__ = "ModRefs"
    id = Column(Integer, primary_key=True)
    module = Column(String)
    mtype = Column(String)
    ref = Column(String)


class ModuleActions(Base):
    __tablename__ = "ModuleActions"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_actions_on_detail_id"


class ModuleArchs(Base):
    __tablename__ = "ModuleArchs"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_archs_on_detail_id"


class ModuleAuthors(Base):
    __tablename__ = "ModuleAuthors"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    name = Column(String)
    email = Column(String)
    # t.index ["detail_id"], name: "index_module_authors_on_detail_id"


class ModuleDetails(Base):
    __tablename__ = "ModuleDetails"
    id = Column(Integer, primary_key=True)
    mtime = Column(DateTime)
    file = Column(String)
    mtype = Column(String)
    refname = Column(String)
    fullname = Column(String)
    name = Column(String)
    rank = Column(Integer)
    description = Column(String)
    license = Column(String)
    privileged = Column(Boolean, unique=False, default=True)
    disclosure_date = Column(String)
    default_target = Column(Integer)
    default_action = Column(String)
    stance = Column(String)
    ready = Column(Boolean, unique=False, default=True)
    # t.index ["description"], name: "index_module_details_on_description"
    # t.index ["mtype"], name: "index_module_details_on_mtype"
    # t.index ["name"], name: "index_module_details_on_name"
    # t.index ["refname"], name: "index_module_details_on_refname"


class ModuleMixins(Base):
    __tablename__ = "ModuleMixins"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_mixins_on_detail_id"


class ModulePlatforms(Base):
    __tablename__ = "ModulePlatforms"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_platforms_on_detail_id"


class ModuleRefs(Base):
    __tablename__ = "ModuleRefs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_refs_on_detail_id"
    # t.index ["name"], name: "index_module_refs_on_name"


class ModuleRuns(Base):
    __tablename__ = "ModuleRuns"
    id = Column(Integer, primary_key=True)
    attempted_at = Column(DateTime, default=datetime.datetime.utcnow)
    fail_detail = Column(String)
    fail_reason = Column(String)
    module_fullname = Column(String)
    port = Column(Integer)
    proto = Column(String)
    session_id = Column(Integer)
    status = Column(String)
    trackable_id = Column(Integer)
    trackable_type = Column(String)
    user_id = Column(Integer)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    # t.index ["session_id"], name: "index_module_runs_on_session_id"
    # t.index ["user_id"], name: "index_module_runs_on_user_id"


class ModuleTargets(Base):
    __tablename__ = "ModuleTargets"
    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer)
    index = Column(Integer)
    name = Column(String)
    # t.index ["detail_id"], name: "index_module_targets_on_detail_id"


class NexposeConsoles(Base):
    __tablename__ = "NexposeConsoles"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    enabled = Column(Boolean, unique=False, default=True)
    owner = Column(String)
    address = Column(String)
    port = Column(Integer)
    username = Column(String)
    password = Column(String)
    status = Column(String)
    version = Column(String)
    cert = Column(String)
    tcached_sites = Column(String)
    name = Column(String)


class Notes(Base):
    __tablename__ = "Notes"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    ntype = Column(String)
    workspace_id = Column(Integer)
    service_id = Column(Integer)
    host_id = Column(Integer)
    updated_at = Column(DateTime)
    critical = Column(Boolean, unique=False, default=True)
    seen = Column(Boolean, unique=False, default=True)
    data = Column(String)
    vuln_id = Column(Integer)
    # t.index ["ntype"], name: "index_notes_on_ntype"
    # t.index ["vuln_id"], name: "index_notes_on_vuln_id"


class Payloads(Base):
    __tablename__ = "Payloads"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    uuid_mask = Column(Integer)
    timestamp = Column(Integer)
    arch = Column(String)
    platform = Column(String)
    urls = Column(String)
    description = Column(String)
    raw_payload = Column(String)
    raw_payload_hash = Column(String)
    build_status = Column(String)
    build_opts = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class Profiles(Base):
    __tablename__ = "Profiles"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    active = Column(Boolean, unique=False, default=True)
    name = Column(String)
    owner = Column(String)
    settings = Column(String)


class Refs(Base):
    __tablename__ = "Refs"
    id = Column(Integer, primary_key=True)
    ref_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    name = Column(String)
    updated_at = Column(DateTime)
    # t.index ["name"], name: "index_refs_on_name"


class ReportTemplates(Base):
    __tablename__ = "ReportTemplates"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    created_by = Column(String)
    path = Column(String)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class Reports(Base):
    __tablename__ = "Reports"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    created_by = Column(String)
    rtype = Column(String)
    path = Column(String)
    options = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    downloaded_at = Column(DateTime)
    task_id = Column(Integer)
    name = Column(String)


class Routes(Base):
    __tablename__ = "Routes"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    subnet = Column(String)
    netmask = Column(String)


class Services(Base):
    __tablename__ = "Services"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    port = Column(Integer)
    proto = Column(String)
    state = Column(String)
    name = Column(String)
    updated_at = Column(DateTime)
    info = Column(String)
    # t.index ["host_id", "port", "proto"], name: "index_services_on_host_id_and_port_and_proto", unique: true
    # t.index ["name"], name: "index_services_on_name"
    # t.index ["port"], name: "index_services_on_port"
    # t.index ["proto"], name: "index_services_on_proto"
    # t.index ["state"], name: "index_services_on_state"


class SessionEvents(Base):
    __tablename__ = "SessionEvents"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    etype = Column(String)
    command = Column(String)
    output = Column(String)
    remote_path = Column(String)
    local_path = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


class Sessions(Base):
    __tablename__ = "Sessions"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    stype = Column(String)
    via_exploit = Column(String)
    via_payload = Column(String)
    desc = Column(String)
    port = Column(Integer)
    platform = Column(String)
    datastore = Column(String)
    opened_at = Column(DateTime)
    closed_at = Column(DateTime)
    close_reason = Column(String)
    local_id = Column(Integer)
    last_seen = Column(DateTime)
    module_run_id = Column(Integer)
    # t.index ["module_run_id"], name: "index_sessions_on_module_run_id"


class Tags(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    desc = Column(String)
    report_summary = Column(Boolean, unique=False, default=True)
    report_detail = Column(Boolean, unique=False, default=True)
    critical = Column(Boolean, unique=False, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class TaskCreds(Base):
    __tablename__ = "TaskCreds"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    cred_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class TaskHosts(Base):
    __tablename__ = "TaskHosts"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    host_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class TaskServices(Base):
    __tablename__ = "TaskServices"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    service_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class TaskSessions(Base):
    __tablename__ = "TaskSessions"
    id = Column(Integer, primary_key=True)

    task_id = Column(Integer)
    session_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    created_by = Column(String)
    module = Column(String)
    completed_at = Column(DateTime)
    path = Column(String)
    info = Column(String)
    description = Column(String)
    progress = Column(Integer)
    options = Column(String)
    error = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    result = Column(String)
    module_uuid = Column(String)
    settings = Column(String)


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    crypted_password = Column(String)
    password_salt = Column(String)
    persistence_token = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    fullname = Column(String)
    email = Column(String)
    phone = Column(String)
    company = Column(String)
    prefs = Column(String)
    admin = Column(Boolean, unique=False, default=True)


class VulnAttempts(Base):
    __tablename__ = "VulnAttempts"
    id = Column(Integer, primary_key=True)
    vuln_id = Column(Integer)
    attempted_at = Column(DateTime, default=datetime.datetime.utcnow)
    exploited = Column(Boolean, unique=False, default=True)
    fail_reason = Column(String)
    username = Column(String)
    module = Column(String)
    session_id = Column(Integer)
    loot_id = Column(Integer)
    fail_detail = Column(String)


class VulnDetails(Base):
    __tablename__ = "VulnDetails"
    id = Column(Integer, primary_key=True)
    vuln_id = Column(Integer)
    cvss_score = Column(Float)
    cvss_vector = Column(String)
    title = Column(String)
    description = Column(String)
    solution = Column(String)
    proof = Column(String)
    nx_console_id = Column(Integer)
    nx_device_id = Column(Integer)
    nx_vuln_id = Column(String)
    nx_severity = Column(Float)
    nx_pci_severity = Column(Float)
    nx_published = Column(DateTime)
    nx_added = Column(DateTime)
    nx_modified = Column(DateTime)
    nx_tags = Column(String)
    nx_vuln_status = Column(String)
    nx_proof_key = Column(String)
    src = Column(String)
    nx_scan_id = Column(Integer)
    nx_vulnerable_since = Column(DateTime)
    nx_pci_compliance_status = Column(String)


class Vulns(Base):
    __tablename__ = "Vulns"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    service_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    name = Column(String)
    updated_at = Column(DateTime)
    info = Column(String)
    exploited_at = Column(DateTime)
    vuln_detail_count = Column(Integer)
    vuln_attempt_count = Column(Integer)
    origin_id = Column(Integer)
    origin_type = Column(String)
    # t.index ["name"], name: "index_vulns_on_name"
    # t.index ["origin_id"], name: "index_vulns_on_origin_id"


class VulnsRefs(Base):
    __tablename__ = "VulnsRefs"
    id = Column(Integer, primary_key=True)
    ref_id = Column(Integer)
    vuln_id = Column(Integer)


class WebForms(Base):
    __tablename__ = "WebForms"
    id = Column(Integer, primary_key=True)
    web_site_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    path = Column(String)
    method = Column(String)
    params = Column(String)
    query = Column(String)
    # t.index ["path"], name: "index_web_forms_on_path"


class WebPages(Base):
    __tablename__ = "WebPages"
    id = Column(Integer, primary_key=True)
    web_site_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    path = Column(String)
    query = Column(String)
    code = Column(Integer)
    cookie = Column(String)
    auth = Column(String)
    ctype = Column(String)
    mtime = Column(DateTime)
    location = Column(String)
    headers = Column(String)
    body = Column(String)
    request = Column(String)
    # t.index ["path"], name: "index_web_pages_on_path"
    # t.index ["query"], name: "index_web_pages_on_query"


class WebSites(Base):
    __tablename__ = "WebSites"
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    vhost = Column(String)
    comments = Column(String)
    options = Column(String)
    # t.index ["comments"], name: "index_web_sites_on_comments"
    # t.index ["options"], name: "index_web_sites_on_options"
    # t.index ["vhost"], name: "index_web_sites_on_vhost"


class WebVulns(Base):
    __tablename__ = "WebVulns"
    id = Column(Integer, primary_key=True)
    web_site_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())

    updated_at = Column(DateTime)
    path = Column(String)
    method = Column(String)
    params = Column(String)
    pname = Column(String)
    risk = Column(Integer)
    name = Column(String)
    query = Column(String)
    category = Column(String)
    confidence = Column(Integer)
    description = Column(String)
    blame = Column(String)
    request = Column(String)
    proof = Column(String)
    owner = Column(String)
    payload = Column(String)
    # t.index ["method"], name: "index_web_vulns_on_method"
    # t.index ["name"], name: "index_web_vulns_on_name"
    # t.index ["path"], name: "index_web_vulns_on_path"


class WmapRequests(Base):
    __tablename__ = "WmapRequests"
    id = Column(Integer, primary_key=True)
    host = Column(String)
    address = Column(String)
    port = Column(Integer)
    ssl = Column(Integer)
    meth = Column(String)
    path = Column(String)
    headers = Column(String)
    query = Column(String)
    body = Column(String)
    respcode = Column(String)
    resphead = Column(String)
    response = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class WmapTargets(Base):
    __tablename__ = "WmapTargets"
    id = Column(Integer, primary_key=True)
    host = Column(String)
    address = Column(String)
    port = Column(Integer)
    ssl = Column(Integer)
    selected = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)


class WorkspaceMembers(Base):
    __tablename__ = "WorkspaceMembers"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(Integer)
    user_id = Column(Integer)


class Workspaces(Base):
    """
    class r
    """

    __tablename__ = "Workspaces"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime)
    boundary = Column(String)
    description = Column(String)
    owner_id = Column(Integer)
    limit_to_network = Column(Boolean, unique=False, default=True)
    import_fingerprint = Column(Boolean, unique=False, default=True)


# Base.metadata.create_all(engine)
