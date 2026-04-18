#!/usr/bin/env python3
"""
Validation script for Module 14.
Checks execution, schema compliance, and quality.
"""

import os
import pathlib
import subprocess
import re
import sys

BASE_DIR = pathlib.Path(__file__).parent
PYTHON = sys.executable  # use the same venv python running this script

def validate_example_execution(example_file: pathlib.Path) -> tuple[bool, str]:
    """Try to execute example file."""
    try:
        result = subprocess.run(
            [PYTHON, str(example_file)],
            capture_output=True,
            timeout=5,
            text=True
        )
        return (result.returncode == 0, result.stdout + result.stderr)
    except subprocess.TimeoutExpired:
        return (False, "Timeout")
    except Exception as e:
        return (False, str(e))


def validate_readme_schema(readme_file: pathlib.Path) -> tuple[int, bool]:
    """Count headings in README and check for 18-heading compliance."""
    content = readme_file.read_text()
    headings = re.findall(r'^#', content, re.MULTILINE)
    # Should have at least 18 headings (title + 7 main sections + subsections)
    return (len(headings), len(headings) >= 18)


def check_for_placeholders(example_file: pathlib.Path) -> bool:
    """Check for TODO or placeholder markers."""
    content = example_file.read_text()
    # Look for TODO, FIXME, pass-only functions, etc.
    bad_patterns = [
        r"TODO",
        r"FIXME",
        r"XXX",
        r"HACK",
    ]
    for pattern in bad_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return False
    return True


def validate_all_topics():
    """Validate all 45 topics."""
    
    topics = sorted([d for d in BASE_DIR.iterdir() if d.is_dir() and d.name[0].isdigit()])
    
    stats = {
        "total": len(topics),
        "examples_executed": 0,
        "examples_passed": 0,
        "schema_compliant": 0,
        "no_placeholders": 0,
        "failures": [],
    }
    
    print("🔍 Validating Module 14...")
    print()
    
    for i, topic_dir in enumerate(topics, 1):
        topic_name = topic_dir.name
        example_file = topic_dir / "examples" / "example_basic.py"
        readme_file = topic_dir / "README.md"
        
        # 1. Check README schema
        heading_count, schema_ok = validate_readme_schema(readme_file)
        if schema_ok:
            stats["schema_compliant"] += 1
        
        # 2. Check for placeholders
        no_placeholders = check_for_placeholders(example_file)
        if no_placeholders:
            stats["no_placeholders"] += 1
        
        # 3. Execute example
        if example_file.exists():
            stats["examples_executed"] += 1
            success, output = validate_example_execution(example_file)
            if success:
                stats["examples_passed"] += 1
                status = "✅"
            else:
                status = "❌"
                stats["failures"].append({
                    "topic": topic_name,
                    "error": output[:100],
                })
        
        # Print progress
        if i % 5 == 0:
            print(f"  [{i:2d}/{len(topics)}] {status} {topic_name}")
    
    print()
    print("=" * 60)
    print("📊 VALIDATION RESULTS")
    print("=" * 60)
    print(f"Total topics:        {stats['total']}")
    print(f"Examples executed:   {stats['examples_executed']}/{stats['total']}")
    print(f"Examples passed:     {stats['examples_passed']}/{stats['examples_executed']}")
    print(f"Schema compliant:    {stats['schema_compliant']}/{stats['total']}")
    print(f"No placeholders:     {stats['no_placeholders']}/{stats['total']}")
    
    if stats["failures"]:
        print()
        print("❌ FAILURES:")
        for failure in stats["failures"][:5]:
            print(f"  - {failure['topic']}: {failure['error'][:60]}")
    
    # Overall status
    all_passed = (
        stats["examples_passed"] == stats["examples_executed"]
        and stats["schema_compliant"] == stats["total"]
        and stats["no_placeholders"] == stats["total"]
    )
    
    print()
    if all_passed:
        print("✅ ALL VALIDATIONS PASSED!")
    else:
        print("⚠️  SOME VALIDATIONS FAILED")
    
    return stats


if __name__ == "__main__":
    stats = validate_all_topics()
