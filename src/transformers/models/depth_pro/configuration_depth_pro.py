# coding=utf-8
# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""DepthPro model configuration"""

from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)


class DepthProConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`DepthProModel`]. It is used to instantiate a
    DepthPro model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the DepthPro
    [apple/DepthPro](https://huggingface.co/apple/DepthPro) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 1024):
            Dimensionality of the encoder layers and the pooler layer.
        fusion_hidden_size
            TODO
        num_hidden_layers (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        mlp_ratio (`int`, *optional*, defaults to 4):
            Ratio of the hidden size of the MLPs relative to the `hidden_size`.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to 224):
            TODO: image_size / 2**n_fusion_blocks = patch_size / patch_embeddings_size
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 14):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        patch_embeddings_size
            TODO
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        layerscale_value (`float`, *optional*, defaults to 1.0):
           Initial value to use for layer scale.
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            Stochastic depth rate per sample (when applied in the main path of residual layers).
        use_swiglu_ffn (`bool`, *optional*, defaults to `False`):
            Whether to use the SwiGLU feedforward neural network.
        apply_layernorm (`bool`, *optional*, defaults to `True`):
            Whether to apply layer normalization to the feature maps in case the model is used as backbone.
        reshape_hidden_states (`bool`, *optional*, defaults to `True`):
            Whether to reshape the feature maps to 4D tensors of shape `(batch_size, hidden_size, height, width)` in
            case the model is used as backbone. If `False`, the feature maps will be 3D tensors of shape `(batch_size,
            seq_len, hidden_size)`.
        intermediate_hook_ids
            TODO
        intermediate_feature_dims
            TODO
        scaled_images_ratios
            TODO
        scaled_images_overlap_ratios
            TODO
        scaled_images_feature_dims
            TODO
        use_batch_norm_in_fusion
            TODO
        use_fov_model
            TODO
        num_fov_head_layers
            TODO

    Example:

    ```python
    >>> from transformers import DepthProConfig, DepthProModel

    >>> # Initializing a DepthPro apple/DepthPro style configuration
    >>> configuration = DepthProConfig()

    >>> # Initializing a model (with random weights) from the apple/DepthPro style configuration
    >>> model = DepthProModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "depth_pro"

    def __init__(
        self,
        hidden_size=1024,
        fusion_hidden_size=256,
        num_hidden_layers=24,
        num_attention_heads=16,
        mlp_ratio=4,
        hidden_act="gelu",
        hidden_dropout_prob=0.0,
        attention_probs_dropout_prob=0.0,
        initializer_range=0.02,
        layer_norm_eps=1e-6,
        image_size=1536,
        patch_size=384,
        num_channels=3,
        patch_embeddings_size=16,
        qkv_bias=True,
        layerscale_value=1.0,
        drop_path_rate=0.0,
        use_swiglu_ffn=False,
        apply_layernorm=True,
        reshape_hidden_states=True,
        intermediate_hook_ids = [11, 5],
        intermediate_feature_dims = [256, 256],
        scaled_images_ratios = [0.25, 0.5, 1],
        scaled_images_overlap_ratios = [0.0, 0.5, 0.25],
        scaled_images_feature_dims = [1024, 1024, 512],
        use_batch_norm_in_fusion=False,
        use_fov_model=True,
        num_fov_head_layers=2,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.hidden_size = hidden_size
        self.fusion_hidden_size = fusion_hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.mlp_ratio = mlp_ratio
        self.hidden_act = hidden_act
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.image_size = image_size
        self.patch_size = patch_size
        self.num_channels = num_channels
        self.patch_embeddings_size = patch_embeddings_size
        self.qkv_bias = qkv_bias
        self.layerscale_value = layerscale_value
        self.drop_path_rate = drop_path_rate
        self.use_swiglu_ffn = use_swiglu_ffn
        self.apply_layernorm = apply_layernorm
        self.reshape_hidden_states = reshape_hidden_states
        self.use_batch_norm_in_fusion = use_batch_norm_in_fusion
        self.use_fov_model = use_fov_model
        self.num_fov_head_layers = num_fov_head_layers
        self.intermediate_hook_ids = intermediate_hook_ids
        self.intermediate_feature_dims = intermediate_feature_dims
        self.scaled_images_ratios = scaled_images_ratios
        self.scaled_images_overlap_ratios = scaled_images_overlap_ratios
        self.scaled_images_feature_dims = scaled_images_feature_dims