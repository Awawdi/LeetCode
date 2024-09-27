import re


def evaluate_deployments(deployments_from_user:list[str]) -> list[str]:
    """
    This function will try to parse the json data and determine number of successful/unsuccessful without using
    the JSON library.

    :param deployments_from_user: json data to be parsed. for example:
    {"deployment_id":"d-123456789", "status":"Success"}
    :return: The result with number of successful, unsuccessful deployments and errors encountered. for example:
    [2,1,0]
    """
    s_count = 0
    f_count = 0
    err_count = 0

    for deploy_string in deployments_from_user:
        try:
            the_id_of_the_deployment = re.search(r'"deployment_id"\s*:\s*"([^"]+)"', deploy_string)
            status_match = re.search(r'"status"\s*:\s*"([^"]+)"', deploy_string)

            if not the_id_of_the_deployment or not status_match:
                err_count += 1
                continue

            deployment_id = the_id_of_the_deployment.group(1)
            status = status_match.group(1)

            if not re.match(r'^d-[a-z0-9]{10}$', deployment_id):
                err_count += 1
                continue

            if status == 'Success':
                s_count += 1
            elif status == 'Fail':
                f_count += 1
            else:
                err_count += 1  # Invalid status
        except Exception:
            err_count += 1

    return [s_count, f_count, err_count]

if __name__ == "__main__":
    deployments_count = int(input("Enter number of deployments and ENTER:").strip())
    deployments = []

    for _ in range(deployments_count):
        deployments_item = input("Enter JSON deployment:").strip()
        deployments.append(deployments_item)

    result = evaluate_deployments(deployments)
    print(result)
