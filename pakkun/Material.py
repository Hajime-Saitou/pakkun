import bpy
from .Origin import Origin
from .NodeTree import NodeTree

class Material(object):
    def __init__(self, material, origin):
        self.material = material
        self.origin = origin

        self.__setProperty(material)

    def __setProperty(self, link):
        pass

    @property
    def nodeTree(self):
        return NodeTree(self.material.node_tree, self.origin)

    @property
    def serialize(self):
        properties = {}

        properties["name"] = self.material.name
        properties["alphaThreshold"] = self.material.alpha_threshold
        properties["blendMethod"] = self.material.blend_method
        properties["diffuseColor"] = tuple(self.material.diffuse_color)
        properties["lineColor"] = tuple(self.material.line_color)
        properties["linePriority"] = self.material.line_priority
        properties["metallic"] = self.material.metallic
        properties["nodeTree"] = self.nodeTree.serialize
        properties["paintActiveSlot"] = self.material.paint_active_slot
        properties["paintCloneSlot"] = self.material.paint_clone_slot
        properties["pass_index"] = self.material.pass_index
        properties["previewRenderType"] = self.material.preview_render_type
        properties["refractionDepth"] = self.material.refraction_depth
        properties["roughness"] = self.material.roughness
        properties["shodowMethod"] = self.material.shadow_method
        properties["showTransparentBack"] = self.material.show_transparent_back
        properties["SpecularColor"] = tuple(self.material.specular_color)
        properties["SpecularInternsity"] = self.material.specular_intensity
        properties["tag"] = self.material.tag
        properties["useBackfaceCulling"] = self.material.use_backface_culling
        properties["useNodes"] = self.material.use_nodes
        properties["usePreviewWorld"] = self.material.use_preview_world
        properties["useScreenRefraction"] = self.material.use_screen_refraction
        properties["useSssTranslucency"] = self.material.use_sss_translucency

        return properties

    def toPrincipledBsdf(self):
        node = self.material.node_tree.nodes.new(type=bpy.types.ShaderNodeBsdfPrincipled.__name__)
        node.inputs["Base Color"].default_value = self.material.diffuse_color
        node.inputs["Metallic"].default_value = self.material.metallic
        node.inputs["Specular"].default_value = self.material.specular_intensity
        node.inputs["Roughness"].default_value = self.material.roughness
        