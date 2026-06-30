-- Tempo account staging and first issue-account mart.
-- This keeps join diagnostics visible: issues without Account and issues whose
-- Account is no longer present in the Tempo account master are retained.

CREATE OR REPLACE VIEW stg_tempo_accounts AS
SELECT
    account_id,
    account_key,
    account_name,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.self')) AS account_self_url,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.status')) AS account_status,
    CAST(JSON_EXTRACT(raw_payload, '$.global') AS UNSIGNED) AS is_global_account,
    CAST(JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.monthlyBudget')) AS DECIMAL(18, 2)) AS monthly_budget,

    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.lead.accountId')) AS lead_account_id,

    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.category.id')) AS category_id,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.category.key')) AS category_key,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.category.name')) AS category_name,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.category.type.name')) AS category_type_name,

    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.customer.id')) AS customer_id,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.customer.key')) AS customer_key,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.customer.name')) AS customer_name,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.contact.displayName')) AS contact_display_name,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.contact.type')) AS contact_type,
    JSON_UNQUOTE(JSON_EXTRACT(raw_payload, '$.links.self')) AS account_links_url,

    raw_payload,
    _loaded_at,
    _dlt_load_id,
    _dlt_id
FROM raw_tempo_accounts;

CREATE OR REPLACE VIEW mart_fact_issue_accounts AS
SELECT
    i.issue_id,
    i.issue_key,
    i.issue_self_url,
    i.summary,
    i.assignee,
    i.reporter,
    i.priority,
    i.resolution,
    i.labels,
    i.linked_issues,
    i.organizations,
    i.created_at,
    i.updated_at,
    i.resolved_at,
    i.due_date,
    i.attivita_su_db,
    i.categoria,
    i.categoria_sql,
    i.comando_sql,
    i.data_tk_axel,
    i.data_stima_approvata,
    i.impatto_incident,
    i.kpi_breached,
    i.oda_ordine_di_acquisto,
    i.presa_in_carico,
    i.processi,
    i.prodotti,
    i.satisfaction,
    i.satisfaction_date,
    i.sla_amco,
    i.sla_ing,
    i.sla_sb,
    i.stima_approvata,
    i.stima_intervento_ore,
    i.priorita_cliente,
    i.sla_ticket,
    i.tempo_di_presa_in_carico,
    i.service_desk_time,
    i.tipo_attivita,
    i.bpo_amco,
    i.bpo_ampre,
    i.bpo_jj_tatooine,
    i.sow_statement_of_work,
    i.data_presa_in_carico,
    i.sla_kpi_presa_in_carico,

    i.issue_type_id,
    i.issue_type_name,
    i.is_subtask,
    i.issue_type_hierarchy_level,

    i.project_id,
    i.project_key,
    i.project_name,
    i.project_type_key,
    i.project_category_id,
    i.project_category_name,

    i.status_id,
    i.status_name,
    i.status_category_id,
    i.status_category_key,
    i.status_category_color,
    i.status_category_name,
    CASE WHEN i.status_category_key = 'done' THEN 1 ELSE 0 END AS is_done,

    i.parent_issue_id,
    i.parent_issue_key,
    i.parent_summary,
    i.parent_issue_type_id,
    i.parent_issue_type_name,
    i.parent_status_id,
    i.parent_status_name,
    i.parent_status_category_key,
    i.parent_status_category_color,
    i.parent_status_category_name,
    i.parent_priority_id,
    i.parent_priority_name,

    i.account_id,
    i.account_name AS jira_account_name,
    a.account_key,
    a.account_self_url,
    COALESCE(a.account_name, i.account_name) AS account_name,
    a.account_status,
    a.is_global_account,
    a.monthly_budget,
    a.lead_account_id,

    a.category_id AS account_category_id,
    a.category_key AS account_category_key,
    a.category_name AS account_category_name,
    a.category_type_name AS account_category_type_name,
    ac.interne_cliente AS account_interne_cliente,
    ac.profit_center AS account_profit_center,
    ac.attivita_specifica AS account_attivita_specifica,
    ac.attivita_generale AS account_attivita_generale,
    ac.specifica_t_e_m AS account_specifica_t_e_m,

    a.customer_id,
    a.customer_key,
    a.customer_name,
    a.contact_display_name,
    a.contact_type,
    a.account_links_url,
    gc.gruppo_cliente,

    CASE WHEN i.account_id IS NOT NULL THEN 1 ELSE 0 END AS issue_has_account_flag,
    CASE WHEN i.account_id IS NOT NULL AND a.account_id IS NOT NULL THEN 1 ELSE 0 END AS account_found_flag,
    CASE
        WHEN i.account_id IS NULL THEN 'missing_on_issue'
        WHEN a.account_id IS NULL THEN 'missing_in_tempo_master'
        ELSE 'found'
    END AS account_resolution_status,

    i._loaded_at AS jira_loaded_at,
    a._loaded_at AS tempo_loaded_at
FROM stg_jira_issues i
LEFT JOIN stg_tempo_accounts a
    ON a.account_id = i.account_id
LEFT JOIN raw_xls_account_category ac
    ON ac.key_category = a.category_key
LEFT JOIN raw_xls_gruppo_cliente gc
    ON UPPER(TRIM(gc.customer_name)) = UPPER(TRIM(a.customer_name));
