// import { AutoTokenizer, AutoModelForSequenceClassification } from '@xenova/transformers';
// import * as tf from '@tensorflow/tfjs'; 

// const model = await AutoModelForSequenceClassification.from_pretrained('Xenova/ms-marco-TinyBERT-L-2-v2');
// const tokenizer = await AutoTokenizer.from_pretrained('Xenova/ms-marco-TinyBERT-L-2-v2');

// const classes = ['POSITIVE', 'NEGATIVE'];

// const inputs = ["I had a terrible day"]

// const features = tokenizer(
//     inputs,
//     {
//         // text_pair: classes,
//         padding: true,
//         truncation: true,
//     }
// )

// const scores = await model(features)

// // Convert logits to probabilities
// const probabilities = tf.softmax(scores.logits);

// // Find the index of the highest probability
// const predictedIndex = probabilities.argMax().dataSync()[0];

// // Map the index to the corresponding class
// const predictedClass = classes[predictedIndex];

// console.log(predictedClass);

import { pipeline } from '@xenova/transformers';

const classifier = await pipeline('sentiment-analysis');
const output = await classifier('I had a terrible day');
console.log(output);

