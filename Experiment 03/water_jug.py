cap_A = 7
cap_B = 3
req = 4

def transfer(from_jug, to_jug, to_jug_capacity):
    return min(from_jug, to_jug_capacity - to_jug)

def water_jug(jug_A, jug_B, procedure):
    if jug_A == req or jug_B == req:
        print(procedure)
        exit(0)
    
    if (jug_A, jug_B) in visited_states:
        return
    
    visited_states.add((jug_A, jug_B))
    
    water_jug(cap_A, jug_B, procedure + '\nFill Jug A')
    water_jug(jug_A, cap_B, procedure + '\nFill Jug B')

    water_jug(0, jug_B, procedure + '\nEmpty Jug A')
    water_jug(jug_A, 0, procedure + '\nEmpty Jug B')

    transfer_amount = transfer(jug_A, jug_B, cap_B)
    water_jug(jug_A - transfer_amount, jug_B + transfer_amount, procedure + '\nTransfer Water from A to B')

    transfer_amount = transfer(jug_B, jug_A, cap_A)
    water_jug(jug_A + transfer_amount, jug_B - transfer_amount, procedure + '\nTransfer Water from B to A')

visited_states = set()
water_jug(0, 0, '')
print('Not found')
