def generate_links():
    years = ['2023', '2024']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    template = f'https://peerlist.io/projects/2023/month/Mar'

    number_of_months = len(months)

    links = []
    # For 2023
    for i in range(2, number_of_months):
        links.append(f'https://peerlist.io/projects/2023/month/{months[i]}')

    # For 2024
    for i in range(0, 5):
        links.append(f'https://peerlist.io/projects/2024/month/{months[i]}')


    return links