actions = []
for _ in range(5):
    actions.append(int(input()))

accepted_hit = set()
for idx in range(4):
    action = actions[idx]
    
    while action <= actions[-1]:
        accepted_hit.add(action)
        action += actions[idx]

print(len(accepted_hit))
    
    
    