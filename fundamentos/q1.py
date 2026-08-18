list = [9,8,7,6,5,4,3,2,1,0]

def analyze_list(nums):
    maior = max(nums)
    menor = min(nums)
    media = sum(nums) / len(nums)
    return maior, menor, media

maior, menor, media = analyze_list(list)

print("Maior número:", maior)
print("Menor número:", menor)
print("Média dos números:", media)