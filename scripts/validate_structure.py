from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    ".gitignore",
    "00_boot/project_boot.md",
    "00_boot/machine_bootstrap.md",
    "00_boot/session_start_protocol.md",
    "01_constitution/chatgpt_native_constitution.md",
    "01_constitution/market_intel_radar_scope.md",
    "01_constitution/operating_principles.md",
    "02_roles/director.md",
    "02_roles/pm.md",
    "02_roles/designer.md",
    "02_roles/advisor.md",
    "02_roles/architect.md",
    "02_roles/vault_coordinator.md",
    "03_workflows/knowledge_studio_pipeline.md",
    "03_workflows/drive_ingestion_workflow.md",
    "03_workflows/source_to_topic_workflow.md",
    "03_workflows/proposal_workflow.md",
    "03_workflows/session_end_reporting.md",
    "04_quality_gates/no_reinvention_rule.md",
    "04_quality_gates/approved_copy_rule.md",
    "04_quality_gates/evidence_quality_rubric.md",
    "04_quality_gates/design_export_checklist.md",
    "04_quality_gates/proposal_review_checklist.md",
    "05_prompt_packs/codex_prompts.md",
    "05_prompt_packs/chatgpt_prompts.md",
    "05_prompt_packs/notion_prompts.md",
    "05_prompt_packs/drive_audit_prompts.md",
    "06_drive_maps/google_drive_structure.md",
    "06_drive_maps/folder_contracts.md",
    "06_drive_maps/path_aliases.example.md",
    "07_locked_decisions/locked_decisions.md",
    "07_locked_decisions/active_projects_index.md",
    "07_locked_decisions/client_language_bank.md",
    "90_templates/session_report_template.md",
    "90_templates/handover_note_template.md",
    "90_templates/instruction_update_template.md",
    "90_templates/codex_task_template.md",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED if not (root / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
