Common:
- Do we need to consider adding confirmation=True for the delete operation
- Filpath to File path
- May I ask is this the tag stored in ARM service? If so, do we need to consider using **tags_type**?
- Do we need these two methods? If not, please delete them
- vm_properties['additionalCapabilities'] = {'ultraSSDEnabled': ultra_ssd_enabled} -> vm_properties['additionalCapabilities']['ultraSSDEnabled'] = ultra_ssd_enabled
- 'hibernation_enabled' to 'enable_hibernation'
- I want to confirm with you that container.name and container_name are not None at any time, right?
- Could you pull the latest code from remote main branch first, and then fix the CI style check issue below. After that, we will help you solve the remaining CI issue later.
- Will the change of parameter type cause breaking change to users?
- Could we add some scenario tests for those new commands?
- Could you please use a specific error type instead of CLIError?
- Could you please address those conflicts?
- Could we abstract it into CLIArgumentType, so that we don't have to define the same flags repeatedly

Azure-cli:
- For [] need check title
- If have mutiple functions, put it in history
- 

Azure-cli-extensions:
- Please write the description of changes into HISTORY,rst and update setup.py to release the new extension version
- 
