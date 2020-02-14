from """①""" import Path

monitored_folder = Path('monitored/')
provided = [file."""②""" for file in list(monitored_folder."""③"""('*.mcl'))]
not_provided = check_company_names(provided)
notify(not_provided)
