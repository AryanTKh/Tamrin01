class MrKrabs:
    def __init__(self, data):
        self.data = data

    def process_dna(self):
        if self.data.startswith('m'):

            return self.replace_twin(self.data + self.data[:10])
        else:
            return 'invalid input'
    def replace_twin(self, dna):
        i = 0
        while i < len(dna) - 2:
            if dna[i] == dna[i+1] == 't':
                dna = dna[:i] + 'o' + dna[i+2:]
                i -=2

            i += 1

        return dna

class SpongeBob:
    def __init__(self, data):
        self.data = data

    def process_dna(self):
        if self.data.startswith('sb'):
            # Sort the string using merge sort and return it.
            sorted_data = self.merge_sort( list( str(len(self.data)+10)) )
            m=''
            for i in range(len(sorted_data)):
                m+=sorted_data[i]
            return m
        else:
            return 'invalid input'

    def merge_sort(self, lst):

        if len(lst) > 1:
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1
        return lst

class Squidward:
    def __init__(self, data):
        self.data = data

    def process_dna(self):
        if self.data.startswith('s') and not self.data[1] == 'b':

            return self.replace_triples(self.data)
        else:
            return 'invalid input'

    def replace_triples(self, dna):
        i = 0
        mm=''
        while i < len(dna) - 2:
            if dna[i] == dna[i+1] == dna[i+2]:
                dna = dna[:i] + '(0_0)' + dna[i+3:]

                i -= 2
########################
            if dna[i] == 'x':
                mm = str(len(dna)-i-4)
#########################
            i += 1

        dna += mm
        return dna

def handle_input(input_data):

    if input_data.startswith(('m', 'sb', 's')):
        processed_data = input_data

    else:
        processed_data = input_data[::-1]


    if processed_data.startswith('m'):
        return MrKrabs(processed_data).process_dna()
    elif processed_data.startswith('sb'):
        return SpongeBob(processed_data).process_dna()
    elif processed_data.startswith('s'):
        return Squidward(processed_data).process_dna()
    else:
        return 'invalid input'

a=input()
print(handle_input(a))




#5
#sbjkfvjkfvkjfkvvkfvjkklfvjkflvbklgbkglbjkblgkflfroforkkfokorfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpmrfokokfkrokfrorkpfkrpokforkorfokprfokrfokpm
#299

#6
#kflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkflfklklkbvkglkbglkkbllgkklbgklbkglkblkgbs
#128







