
def get_topic_image(topic):
    topic = topic.lower()
    image_map = {
        "biology": "images/biology_cell.png",
        "geometry": "images/triangle_types.png",
        "chemistry": "images/atom_structure.png",
        "civics": "images/us_branches.png"
    }
    return image_map.get(topic, "")
