
from .formatters import *


def assemble(template_name, data, theme):
    if template_name == "project_card":
        template_data = {
            "name": format_title(data["name"]),


            "stars": format_number(data["stargazers_count"]),
            "forks": format_number(data["forks_count"]),
            "watch": format_number(data["watchers"]),

            "size": format_file(data["size"]),
            "issues": data["open_issues"],
            "lang": data["language"],
            "license": format_license(data["license"]["name"]) if data["license"] else "Unknown",

            "created": format_date(data["created_at"]),
            "updated": format_date(data["updated_at"]),
        }
        template_data["desc1"], template_data["desc2"], template_data["desc3"] = format_desc(
            data["description"] if data["description"] else "~")
        template_data.update(theme)
        return template_data
