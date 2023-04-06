def infura_acc():

    key_path = "./scripts/certificate_processing/infura_project_details.txt"
    keys = []

    with open(key_path, 'r') as f:
        for line in f:
            keys.append(line.strip())

    projectId = keys[0]
    projectSecret = keys[1]
    
    return projectId, projectSecret