class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def convert(num):
            real, img = num.split('+')
            real = int(real)
            img = int(img[:-1])
            return real, img
        real_1, img_1 = convert(num1)
        real_2, img_2 = convert(num2)
        answer = f'{(real_1*real_2) - (img_1*img_2)}+{img_1*real_2 + img_2*real_1}i'
        return answer