
#merger.py- BUGGY version
def merge_configs(base:dict, override:dict) -> dict:
  result=base.copy()
  result.update(override)
  return result
