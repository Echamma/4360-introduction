import sys



options = {'/fact': "I like potatoes", 
           '/why': 'I like the software part of comuters more than the hardware part',
           '/what':'hopefully work at a company that helps the environment, or make money and live comfortably',
           '/name': 'Elias Chamma, I am a senior'}


def main():
    if len(sys.argv)>1:
        command = sys.argv[1]
        try:
            print(options[command])
        except:
            print('there has been an error that option is not available :D  the options are \n \'/fact\' \n \'/why\' \n \'/what\' \n \'/name\'')
    else:
        print("botato")

if __name__ == "__main__":
    main()
