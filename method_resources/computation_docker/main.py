import os
import fasttext
import codecs 
import sys

if __name__ == "__main__":
    
    with codecs.open(sys.argv[1], "r", encoding = "utf-8") as f:
        lines = f.readlines()

    #LID2 Constants
    model = fasttext.load_model("model.lid.top800.epoch20.neg100.dim100.ns.small.min5.ftz")

    predictions = []
    for line in open(sys.argv[1]):
        # strip \n from line
        line = line.rstrip("\n")
        pred_label = model.predict(line)
        predictions.append(pred_label)

    # write predictions to file
    with open("output/fastText_predictions.txt", "w") as f:
        for pred in predictions:
            # Write prediction to file, and remove __label__ prefix
            f.write(pred[0][0].replace("__label__", "") + "\n")
