from django.db import models

# Create your models here.


class CodigoMorse(models.Model):
    """A class used to represent an Morse Code

    Attributes
    ----------
    character : str
        a alphanumeric string [A-Z][0-9]
    code : str
        a representaton on morse code from character only admits ['.','-']

    Methods
    -------
    decodeBits2Morse(binary)
        Decode a binary message to morse code
    translate2Morse(human)
        Translate a alphanumeric message to morse code representation
    translate2Human(morse)
        Translate morse code message to an alphanumeric representation
    """

    character = models.CharField(max_length=1)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.character}: {self.code}"

    @classmethod
    def get_code_dict(self):
        """Create a dictionary with the elements of type CodigoMorse

        Returns
        -------
        dict
            A dict of containing alphanumeric key with its corresponding morse code as value
        """
        return {code.character: code.code for code in self.objects.all()}

    @classmethod
    def __return_letter(self, letter):
        """Search the morse representation of a alphanumeric character

        Parameters
        ----------
        letter : str
            A alphanumeric character [A-Z][0-9]

        Returns
        -------
        str
            A string of morse code representation of the letter parameter
        """
        dict_morse = self.get_code_dict()
        res = ''
        try:
            keys = list(dict_morse.keys())
            values = list(dict_morse.values())
            res = keys[values.index(letter)]
        except Exception as e:
            raise letter
        return res

    @staticmethod
    def __find_greatest_separator(lista):
        """Find the largest substring fo zeros

        Parameters
        ----------
        lista : array
            A list of strings that coitains zeros and ones, only one type per element i.e. ['000','111']
        
        Returns
        -------
        str
            A string of morse code representation of the letter parameter
        """

        sep = ''
        for i in lista:
            if '0' in i and len(i) > len(sep):
                sep = i
        return sep

    @classmethod
    def __get_indixes(self, lista, min_leght):
        """Search all the coincidenes of the separator of zeros

        Parameters
        ----------
        lista : array
            A list of strings that coitains zeros and ones, only one type per element i.e. ['000','111']
        min_lenght : int
            The minimum lenght of the separators

        Returns
        -------
        array
            A array of integers corresponding to the position of all the coincidences
        """
        indixes = []
        sep = self.__find_greatest_separator(lista)
        print('--->>',sep, lista)
        for reps in range(len(sep), min_leght-1, -1):
            indixes += [idx for idx,
                        val in enumerate(lista) if val == '0'*reps]
        indixes.sort()
        return indixes

    @classmethod
    def __split_words_letters(self, lista, min_leght):
        """Recursive function tha classify the input array (lista) into words

        Parameters
        ----------
        lista : array
            A list of strings that coitains zeros and ones, only one type per element i.e. ['000','111']
        min_lenght : array
            A Array of integers which are the minimum lenght of the separators on each level

        Returns
        -------
        array
            A array of strings classified into words
        """
        indixes = self.__get_indixes(lista, min_leght[0])
        if len(min_leght) == 1:
            if len(indixes) == 0:
                return [lista]
            aux = [lista[:indixes[0]]] if lista[:indixes[0]] else []
            for i in range(len(indixes)-1):
                aux.append(lista[indixes[i]+1:indixes[i+1]])
            aux.append(lista[indixes[-1]+1:]
                       ) if lista[indixes[-1]+1:] else None
            return aux
        else:
            aux = [self.__split_words_letters(
                lista[:indixes[0]], min_leght[1:])] if lista[:indixes[0]] else []
            for i in range(len(indixes)-1):
                aux.append(self.__split_words_letters(
                    lista[indixes[i]+1:indixes[i+1]], min_leght[1:]))
            aux.append(self.__split_words_letters(
                lista[indixes[-1]+1:], min_leght[1:])) if lista[indixes[-1]+1:] else None
            return aux

    @staticmethod
    def __to_list(cad):
        """Groups the input string into zeros and ones

        Parameters
        ----------
        cad : str
            A numeric strign with only zeros and ones

        Returns
        -------
        array
            A array of strings divided into zeros and ones i.e. ['11','000']
        """
        lista = []
        aux1 = cad[0]
        aux2 = cad[0]
        for i in range(1, len(cad)):
            if cad[i] == aux1:
                aux2 += cad[i]
                if i == len(cad)-1:
                    lista.append(aux2)
            else:
                lista.append(aux2)
                aux2 = cad[i]
            aux1 = cad[i]
        return lista

    @classmethod
    def translate2Human(self, morse):
        """Translate morse code message to an alphanumeric representation

        Parameters
        ----------
        morse : str
            A morse code message

        Returns
        -------
        str
           A alphanumeric representation of the input message
        """
        print('11111111111')
        if morse:
            print('22222222222')
            morse_list = map(lambda m:  m.split(' '), morse.split('   '))
            print('333333333333', morse_list)
            return ' '.join([''.join(map(self.__return_letter, word)) for word in morse_list])
        return ''

    @classmethod
    def translate2Morse(self, human):
        """Translate a alphanumeric message to morse code representation

        Parameters
        ----------
        human : str
            A alphanumeric message

        Returns
        -------
        str
           A morse code representaton of the input message
        """
        dict_morse = self.get_code_dict()
        if human:
            return ' '.join([dict_morse.get(h) if dict_morse.get(h) else '' for h in human.upper()])
        return ''

    @classmethod
    def decodeBits2Morse(self, binary):
        """Decode a binary message to morse code

        Parameters
        ----------
        binary : str
            A binary message simulating morse code
        
        Returns
        -------
        str
           A morse code representaton of the input message
        """
        cad = ''
        if binary:
            words = self.__split_words_letters(self.__to_list(binary), [8, 4])
            print(words)
            for idx1, word in enumerate(words):
                for idx2, letter in enumerate(word):
                    for l in letter:
                        if "1" in l:
                            cad += '.' if len(l) <= 5 else '-'
                    cad += ' ' if idx2 < len(word)-1 else ''
                cad += '   ' if idx1 < len(words)-1 else ''
        return cad


class WordsTable(models.Model):
    """A class used to represent an Morse Code

    Attributes
    ----------
    word : str
        A alphanumeric string [A-Z][0-9]
    morse : str
        A representaton on morse code from word attribute
    frequency : int
        The frequency of the word

    Methods
    -------
    create(word, morse, frequency)
        Return new instance of WordsTable
    update_words(words)
        Update the words at the WordsTable model
    """

    word = models.CharField(max_length=20)
    morse = models.CharField(max_length=100)
    frequency = models.IntegerField()

    def __str__(self):
        return f"{self.word} ({self.morse}): {self.frequency}"

    @classmethod
    def create(self, word, morse, frequency):
        """Return new instance of WordsTable

        Parameters
        ----------
        word : str
            A alphanumeric string [A-Z][0-9]
        morse : str
            A representaton on morse code from word attribute
        frequency : int
            The frequency of the word
        
        Returns
        -------
        WordsTable
           New instance of WordsTable
        """
        return self(word=word, morse=morse, frequency=frequency)

    @classmethod
    def update_words(self, words):
        if words:
            frecuency_words = {}
            for w in words.split(' '):
                if w in frecuency_words:
                    frecuency_words[w] += 1
                else:
                    frecuency_words[w] = 1
            for key, val in frecuency_words.items():
                if self.objects.filter(word=key).exists():
                    word = self.objects.get(word=key)
                    word.frequency += val
                    word.save()
                else:
                    word = self.create(
                        word=key, morse=CodigoMorse.translate2Morse(key), frequency=val)
                    word.save()

