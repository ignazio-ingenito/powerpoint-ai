-- MariaDB single-database layout.
-- Logical layers are represented by table prefixes:
-- raw_, ref_, stg_, mart_.

CREATE TABLE IF NOT EXISTS ref_jira_account_sap_wbs_mapping (
    mapping_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    jira_account TEXT NOT NULL,
    jira_account_description TEXT,
    axel_order TEXT,
    sap_contract TEXT,
    sap_project TEXT,
    sap_wbs_code TEXT NOT NULL,
    sap_wbs_description TEXT,
    initiative_link TEXT,
    opened_date DATE,
    closed_date DATE,
    account_status TEXT,
    open_unique_key VARCHAR(1024)
        GENERATED ALWAYS AS (
            CASE
                WHEN closed_date IS NULL
                    AND LOWER(TRIM(jira_account)) NOT IN ('', 'non serve', 'x')
                    AND LOWER(TRIM(sap_wbs_code)) NOT IN ('', 'non serve', 'x')
                THEN CONCAT(jira_account, '|', sap_wbs_code)
                ELSE NULL
            END
        ) STORED
);

CREATE INDEX IF NOT EXISTS idx_ref_jira_account_sap_wbs_mapping_account
    ON ref_jira_account_sap_wbs_mapping (jira_account);

CREATE INDEX IF NOT EXISTS idx_ref_jira_account_sap_wbs_mapping_wbs
    ON ref_jira_account_sap_wbs_mapping (sap_wbs_code);

CREATE UNIQUE INDEX IF NOT EXISTS uq_ref_jira_account_sap_wbs_mapping_open
    ON ref_jira_account_sap_wbs_mapping (open_unique_key);

CREATE TABLE IF NOT EXISTS ref_resource_organization_mapping (
    mapping_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    jira_resource_name TEXT NOT NULL,
    sap_resource_name TEXT,
    canonical_resource_name TEXT,
    resource_status TEXT,
    resource_category TEXT,
    company TEXT,
    team_name TEXT,
    area_name TEXT,
    novigo_role_current TEXT,
    novigo_role_previous TEXT,
    capacity_role_primary TEXT,
    capacity_role_secondary TEXT,
    resource_type TEXT,
    jira_account_id TEXT,
    sap_personnel_number TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    work_hours_per_day NUMERIC(5, 2),
    check_hours_flag BOOLEAN,
    manager_name TEXT,
    manager_sap_name TEXT,
    act_type TEXT,
    internship_start_date DATE,
    internship_end_date DATE,
    hiring_date DATE,
    contract_expiration_date DATE,
    termination_date DATE
);

CREATE INDEX IF NOT EXISTS idx_ref_resource_organization_mapping_jira_account
    ON ref_resource_organization_mapping (jira_account_id);

CREATE INDEX IF NOT EXISTS idx_ref_resource_organization_mapping_sap_personnel
    ON ref_resource_organization_mapping (sap_personnel_number);

CREATE INDEX IF NOT EXISTS idx_ref_resource_organization_mapping_resource_name
    ON ref_resource_organization_mapping (jira_resource_name);

CREATE INDEX IF NOT EXISTS idx_ref_resource_organization_mapping_team_area
    ON ref_resource_organization_mapping (team_name, area_name);
