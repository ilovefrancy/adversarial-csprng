"""The operations.py module contains definitions of symbolic
Tensor operations that can be used as part of a Keras/TensorFlow
model, for example in a Keras Lambda layer.
"""

import tensorflow as tf


def drop_last_value(original_size, batch_size):
    """Returns a closure that operates on Tensors. It is
    used to connect the GAN's generator to the predictor,
    as the discriminator receives the generator's output
    minus the last bit."""
    def layer(x: tf.Tensor):
        return tf.strided_slice(tf.reshape(x, [tf.shape(x)[0], original_size]), [0, 0], [batch_size, -1], [1, 1])
    return layer
