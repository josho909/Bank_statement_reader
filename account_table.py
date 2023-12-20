account_table = pd.DataFrame(
                    {
                        'account_name': ['Offset', 'Fixed', 'Variable'],
                        'position_number': [1,2,3]
                    }
                )
account_table = account_table.set_index('account_name')