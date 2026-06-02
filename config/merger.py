def merge_configs(base:dict,override: dict)-> dict:
    result=base.copy()
    for key ,value in override.items():
      if key in result and isinstance(result[key],dict) and isinstance(value,dict):
          result[key] =merge_config(result[key],value)
      else:
        result[key]=value
      return result 
    
