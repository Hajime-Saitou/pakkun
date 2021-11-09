import sys
from .NodeSocket import NodeSocket

class NodeBase(object):
    def __init__(self, node, origin):
        self.node = node
        self.origin = origin

        self.__setProperty(node)

    def __setProperty(self, node):
        self.name = node.name

    @property
    def index(self) -> int:
        return [ node.as_pointer() for node in self.node.id_data.nodes ].index(self.node.as_pointer())

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["name"] = self.name
        properties["color"] = tuple(self.node.color)
        properties["dimensions"] = tuple(self.node.dimensions)
        properties["height"] = self.node.height
        properties["hide"] = self.node.hide
        properties["inputs"] = [ socket.serialize for socket in [ NodeSocket(socket) for socket in self.node.inputs ] if socket.serializable ]
        properties["label"] = self.node.label
        properties["location"] = tuple(self.node.location)
        properties["mute"] = self.node.mute
        properties["label"] = self.node.label
        properties["outputs"] = [ socket.serialize for socket in [ NodeSocket(socket) for socket in self.node.outputs ] if socket.serializable ]
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

    @property
    def thereLinkedInInputs(self) -> bool:
        return sum([ len(input.links) for input in self.node.inputs ]) != 0

    @property
    def thereLinkedInOutputs(self) -> bool:
        return sum([ len(output.links) for output in self.node.outputs ]) != 0

    @property
    def dangled(self) -> bool:
        return not (self.thereLinkedInInputs | self.thereLinkedInOutputs)

    @property
    def thereHaveLinkErrorInInputs(self) -> bool:
        return False in [ link.is_valid for link in [ input.links[0] for input in self.node.inputs if input.links ]]

    @property
    def thereHaveLinkErrorInOutputs(self) -> bool:
        return False in [ link.is_valid for link in [ output.links[0] for output in self.node.outputs if output.links ]]

    @property
    def linkedError(self) -> bool:
        return self.thereHaveLinkErrorInInputs | self.thereHaveLinkErrorInOutputs

class Node(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)

    @property
    def subNodeClass(self):
        return getattr(sys.modules[__name__], f"{type(self.node).__name__}")(self.node, self.origin)

    @property
    def serialize(self) -> dict:
        properties = super().serialize
        properties |= self.subNodeClass.serialize
        return properties

    @property
    def category(self) -> str:
        return self.subNodeClass.category

class NodeFrame(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Layout"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class NodeGroupInput(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Group"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class NodeGroupOutput(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Group"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class NodeReroute(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Layout"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeAddShader(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeAmbientOcclusion(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

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
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["attributeType"] = self.node.attribute_type
        properties["attributeName"] = self.node.attribute_name
        return properties

class ShaderNodeBackground(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Layout"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBevel(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["samples"] = self.node.samples

        return properties

class ShaderNodeBlackbody(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBrightContrast(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfAnisotropic(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfDiffuse(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfGlass(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfGlossy(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfHair(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfHairPrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfPrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        properties["subsurfaceMethod"] = self.node.subsurface_method
        return properties

class ShaderNodeBsdfRefraction(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        properties["distribution"] = self.node.distribution
        return properties

class ShaderNodeBsdfToon(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfTranslucent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfTransparent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBsdfVelvet(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeBump(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["Invert"] = self.node.invert
        return properties

class ShaderNodeCameraData(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeClamp(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        properties["clampType"] = self.node.clamp_type
        return properties

class ShaderNodeCombineHSV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCombineRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCombineXYZ(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeCustomGroup(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Group"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeDisplacement(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["space"] = self.node.space
        return properties

class ShaderNodeEeveeSpecular(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeEmission(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeFresnel(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeGamma(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeGroup(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Group"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHairInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHoldout(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeHueSaturation(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeInvert(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLayerWeight(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLightFalloff(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeLightPath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeMapRange(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        properties["interpolationType"] = self.node.interpolation_type
        properties["clamp"] = self.node.clamp
        return properties

class ShaderNodeMapping(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["vectorType"] = self.node.vector_type
        return properties

class ShaderNodeMath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        properties["operation"] = self.node.operation
        properties["useClamp"] = self.node.use_clamp

        return properties

class ShaderNodeMixRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        properties["blendType"] = self.node.blend_type
        properties["useClamp"] = self.node.use_clamp
        return properties

class ShaderNodeMixShader(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNewGeometry(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNormal(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeNormalMap(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["space"] = self.node.space
        properties["uvMap"] = self.node.uv_map
        return properties

class ShaderNodeObjectInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputAOV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Output"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputLight(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputLineStyle(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeOutputMaterial(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Output"

    @property
    def serialize(self):
        properties = super().serialize
        properties["target"] = self.node.target
        return properties

class ShaderNodeOutputWorld(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeParticleInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeRGBCurve(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Color"

    @property
    def serialize(self):
        properties = super().serialize
        properties["color"] = tuple(self.node.color)
        properties["mapping"] = self.serializeCurveMapping(self.node.mapping)
        return properties

    def serializeCurveMapping(self, mapping) -> dict:
        properties = {}
        properties["blackLevel"] = tuple(mapping.black_level)
        properties["clipMaxX"] = mapping.clip_max_x
        properties["clipMaxY"] = mapping.clip_max_y
        properties["clipMinX"] = mapping.clip_min_x
        properties["clipMinY"] = mapping.clip_min_y
        properties["curves"] = self.serializeCurves(mapping.curves)
        properties["extend"] = mapping.extend
        properties["tone"] = mapping.tone
        properties["useClip"] = mapping.use_clip
        properties["whiteLevel"] = tuple(mapping.white_level)
        
        return properties

    def serializeCurves(self, curves) -> list:
        properties = []
        for curve in curves:
            properties.append({ "points": self.serializeCurvePoints(curve.points) })
        return properties

    def serializeCurvePoints(self, points) -> list:
        properties = []
        for point in points:
            properties.append(self.serializeCurvePoint(point))
        return properties

    def serializeCurvePoint(self, point) -> dict:
        properties = {}
        properties["handleType"] = point.handle_type
        properties["location"] = tuple(point.location)
        properties["select"] = point.select
        
        return properties

class ShaderNodeRGBToBW(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeScript(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Script"

    @property
    def serialize(self):
        properties = super().serialize
        properties["mode"] = self.node.mode
        properties["scriptName"] = self.node.script.name
        return properties

class ShaderNodeSeparateHSV(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSeparateRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSeparateXYZ(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeShaderToRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSqueeze(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeSubsurfaceScattering(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        properties["falloff"] = self.node.falloff
        return properties

class ShaderNodeTangent(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["axis"] = self.node.axis
        properties["directionType"] = self.node.direction_type

        return properties

class ShaderNodeTexBrick(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["offset"] = self.node.offset
        properties["offsetFrequency"] = self.node.offset_frequency
        properties["squash"] = self.node.squash
        properties["squashFrequency"] = self.node.squash_frequency
        return properties

class ShaderNodeTexChecker(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeTexCoord(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["objectName"] = self.node.object.name if self.node.object else ""
        properties["fromInstancer"] = self.node.from_instancer
        return properties

class ShaderNodeTexEnvironment(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["imageName"] = self.node.image.name if self.node.image else ""
        properties["interpolation"] = self.node.interpolation
        properties["projection"] = self.node.projection
        return properties

class ShaderNodeTexGradient(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["gradientType"] = self.node.gradient_type
        return properties

class ShaderNodeTexIES(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["mode"] = self.node.mode
        properties["ies"] = self.node.ies if self.node.ies else ""
        return properties

class ShaderNodeTexImage(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["imageName"] = self.node.image.name if self.node.image else ""
        properties["interpolation"] = self.node.interpolation
        properties["projection"] = self.node.projection
        properties["extension"] = self.node.extension
        return properties

class ShaderNodeTexMagic(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["turbulenceDepth"] = self.node.turbulence_depth
        return properties

class ShaderNodeTexMusgrave(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["musgraveDimensions"] = self.node.musgrave_dimensions
        properties["musgraveType"] = self.node.musgrave_type
        return properties

class ShaderNodeTexNoise(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["noiseDimensions"] = self.node.noise_dimensions
        return properties

class ShaderNodeTexPointDensity(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["pointSource"] = self.node.point_source
        properties["objectName"] = self.node.object.name if self.node.object else ""
        properties["space"] = self.node.space
        properties["radius"] = self.node.radius
        properties["interpolation"] = self.node.interpolation
        properties["resolution"] = self.node.resolution
        properties["particleColorSource"] = self.node.particle_color_source
        return properties

class ShaderNodeTexSky(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["skyType"] = self.node.sky_type
        properties["sunDisc"] = self.node.sun_disc
        properties["sunSize"] = self.node.sun_size
        properties["sunIntensity"] = self.node.sun_intensity
        properties["sunElevation"] = self.node.sun_elevation
        properties["sunRotation"] = self.node.sun_rotation
        properties["altitude"] = self.node.altitude
        properties["airDensity"] = self.node.air_density
        properties["dustDensity"] = self.node.dust_density
        properties["ozoneDensity"] = self.node.ozone_density
        return properties

class ShaderNodeTexVoronoi(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["voronoiDimensions"] = self.node.voronoi_dimensions
        properties["feature"] = self.node.feature
        properties["distance"] = self.node.distance
        return properties

class ShaderNodeTexWave(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["waveType"] = self.node.wave_type
        properties["bandsDirection"] = self.node.bands_direction
        properties["waveProfile"] = self.node.wave_profile
        return properties

class ShaderNodeTexWhiteNoise(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Texture"

    @property
    def serialize(self):
        properties = super().serialize
        properties["noiseDimensions"] = self.node.noise_dimensions
        return properties

class ShaderNodeTree(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeUVAlongStroke(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Undefined"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeUVMap(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["fromInstancer"] = self.node.from_instancer
        properties["uvMap"] = self.node.uv_map
        return properties

# Color Ramp
class ShaderNodeValToRGB(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeValue(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorCurve(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorDisplacement(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["space"] = self.node.space
        return properties

class ShaderNodeVectorMath(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVectorRotate(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["rotarionType"] = self.node.rotation_type
        properties["invert"] = self.node.invert
        return properties

class ShaderNodeVectorTransform(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Vector"

    @property
    def serialize(self):
        properties = super().serialize
        properties["vectorType"] = self.node.vector_type
        properties["convertFrom"] = self.node.convert_from
        properties["convertTo"] = self.node.convert_to
        return properties

class ShaderNodeVertexColor(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["layerName"] = self.node.layer_name
        return properties

class ShaderNodeVolumeAbsorption(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumeInfo(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumePrincipled(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeVolumeScatter(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Shader"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeWavelength(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Converter"

    @property
    def serialize(self):
        properties = super().serialize
        return properties

class ShaderNodeWireframe(NodeBase):
    def __init__(self, node, origin):
        super().__init__(node, origin)
        self.category = "Input"

    @property
    def serialize(self):
        properties = super().serialize
        properties["usePixelSize"] = self.node.use_pixel_size
        return properties
