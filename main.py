import sys
from input_output import load_image, save_image
from commands.help import do_help
from commands.histogram import do_histogram

COMMANDS = {
    "--histogram" : do_histogram,
}

SIMILARITY = {

}


if len(sys.argv) == 1:
    print("No command line parameters given.\n")
    sys.exit()

command = sys.argv[1]

if command == '--help':
    do_help()

else:
    if len(sys.argv) == 2:
        print("Too few command line parameters given.\n")
        sys.exit()

    args = {}
    for arg in sys.argv[2:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
            args[key] = value
        else:
            print("Invalid argument:" + arg)

    if command in SIMILARITY:
        original = load_image(args.get('-original'))
        other = load_image(args.get('-other'))
        value = SIMILARITY[command](original, other)
        print(str(round(value,4)))
        
    else:
        input_path = args.get('-input')
        output_path = args.get('-output')

        im = load_image(input_path)
        try:
            newIm = COMMANDS[command](im, args)
            save_image(output_path, newIm)

        except KeyError:
            print("Command not found.\n")

    print("")


