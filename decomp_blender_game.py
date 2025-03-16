def decomp_blender_game(filePath, outputFilePath):
    try:
        with open(filePath, 'rb') as f:
            fileData = f.read()

        # Find the position of the string "BLENDER-"
        searchString = b"BLENDER-"
        position = fileData.find(searchString)

        if position == -1:
            print(f"String '{searchString.decode()}' not found in the file.")
            return

        trimmedData = fileData[position:] # Keep everything from the found position onwards

        # Write the result to the output file
        with open(outputFilePath, 'wb') as f_out:
            f_out.write(trimmedData)

        print(f"Processed file saved as: {outputFilePath}")

    except FileNotFoundError:
        print(f"File '{filePath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("This ONLY \"decompiles\" games made in The BLENDER GAME ENGINE.\n")
inputFile = input("Enter the PATH to the game's executable: ")
outputFile = input("Enter the PATH AND NAME of the output file (without \'.blend\'): ")
outputFile += ".blend"

decomp_blender_game(inputFile, outputFile)