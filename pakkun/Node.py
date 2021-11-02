import sys
from .NodeIos import NodeIos

class NodeBase(object):
    def __init__(self, node, origin):
        self.node = node
        self.origin = origin

        self.__setProperty(node)

    def __setProperty(self, node):
        self.name = node.name

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["name"] = self.name
        properties["color"] = tuple(self.node.color)
        properties["dimensions"] = tuple(self.node.dimensions)
        properties["height"] = self.node.height
        properties["hide"] = self.node.hide
        properties["inputs"] = [ ios.serialize for ios in [ NodeIos(ios) for ios in self.node.inputs ] if ios.serializable ]
        properties["label"] = self.node.label
        properties["location"] = tuple(self.node.location)
        properties["mute"] = self.node.mute
        properties["label"] = self.node.label
        properties["outputs"] = [ ios.serialize for ios in [ NodeIos(ios) for ios in self.node.outputs ] if ios.serializable ]
        properties["parentName"] = self.node.parent.name if self.node.parent else ""
        properties["select"] = self.node.select
        properties["showOptions"] = self.node.show_options
        properties["showPreview"] = self.node.show_preview
        properties["showTexture"] = self.node.show_texture
        properties["type"] = self.node.type
        properties["useCustomColor"] = self.node.use_custom_color
        properties["width"] = self.node.width
        properties["widthHidden"] = self.node.width_hidden

        return properties

class Node(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self) -> dict:
        properties = super().serialize
        properties |= getattr(sys.modules[__name__], f"{type(self.node).__name__}")(self.node, self.origin).serialize
        return properties

class ShaderNodeAddShader(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeAmbientOcclusion(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["inside"] = self.node.inside
        properties["onlyLocal"] = self.node.only_local
        properties["samples"] = self.node.samples

        return properties

class ShaderNodeAttribute(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["attributeType"] = self.node.attribute_type
        properties["attributeName"] = self.node.attribute_name
        return properties

class ShaderNodeBackground(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBevel(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["samples"] = self.node.samples

        return properties

class ShaderNodeBlackbody(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBrightContrast(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties
class ShaderNodeBsdfAnisotropic(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfDiffuse(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfGlass(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfGlossy(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfHair(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfHairPrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfPrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        properties["subsurfaceMethod"] = self.node.subsurface_method
        return properties

class ShaderNodeBsdfRefraction(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfToon(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfTranslucent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfTransparent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfVelvet(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBump(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties
class ShaderNodeCameraData(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeClamp(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCombineHSV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCombineRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCombineXYZ(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCustomGroup(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeDisplacement(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeEeveeSpecular(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeEmission(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeFresnel(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeGamma(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeGroup(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHairInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHoldout(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHueSaturation(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeInvert(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLayerWeight(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLightFalloff(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLightPath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeMapRange(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeMapping(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeMath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["useClamp"] = self.node.use_clamp

        return properties

class ShaderNodeMixRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeMixShader(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNewGeometry(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNormal(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNormalMap(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeObjectInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputAOV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputLight(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputLineStyle(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputMaterial(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["target"] = self.node.target
        return properties

class ShaderNodeOutputWorld(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeParticleInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeRGBCurve(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeRGBToBW(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeScript(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSeparateHSV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSeparateRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSeparateXYZ(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeShaderToRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSqueeze(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSubsurfaceScattering(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["falloff"] = self.node.falloff
        return properties

class ShaderNodeTangent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["axis"] = self.node.axis
        properties["directionType"] = self.node.direction_type

        return properties

class ShaderNodeTexBrick(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexChecker(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexCoord(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["objectName"] = self.node.object.name if self.node.object else ""
        properties["fromInstancer"] = self.node.from_instancer
        return properties

class ShaderNodeTexEnvironment(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexGradient(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexIES(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexImage(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexMagic(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexMusgrave(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexNoise(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexPointDensity(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexSky(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexVoronoi(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexWave(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexWhiteNoise(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTree(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeUVAlongStroke(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeUVMap(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["fromInstancer"] = self.node.from_instancer
        properties["uvMap"] = self.node.uv_map
        return properties

class ShaderNodeValToRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeValue(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorCurve(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorDisplacement(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorMath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorRotate(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorTransform(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVertexColor(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["layerName"] = self.node.layer_name
        return properties

class ShaderNodeVolumeAbsorption(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumeInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumePrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumeScatter(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeWavelength(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeWireframe(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def serialize(self):
        properties = super().serialize
        properties["usePixelSize"] = self.node.use_pixel_size
        return properties
