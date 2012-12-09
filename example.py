from ach.builder import AchFile

settings = {
    'immediate_dest' : '123456789',
    'immediate_org' : '123456789',
    'immediate_dest_name' : 'YOUR BANK',
    'immediate_org_name' : 'YOUR COMPANY',
    'company_id' : '1234567890', #tax number
}

ach_file = AchFile('A', settings) #file Id mod

entries = [
    {
        'type'           : '22', # type of
        'routing_number' : '12345678',
        'account_number' : '11232132',
        'amount'         : '10.00',
        'name'           : 'Alice Wanderdust',
    },
    {
        'type'           : '22',
        'routing_number' : '12345678',
        'account_number' : '234234234',
        'amount'         : '150.00',
        'name'           : 'Billy Holiday',
    },
    {
        'type'           : '22',
        'routing_number' : '12323231',
        'account_number' : '123123123',
        'amount'         : '12.13',
        'name'           : 'Rachel Welch',
    },
]

ach_file.add_batch('PPD',entries,credits=True)

print ach_file.render_to_string()
