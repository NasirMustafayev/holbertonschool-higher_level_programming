#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types")
        return
    
    if len(template) == 0:
        print("Template is empty, no output files generated.")

    if len(attendees) == 0:
        print("No data provided, no output files generated.")

    for attendee in attendees:
        attendee_number = attendees.index(attendee) + 1
        content = template

        name_val = attendee['name'] if 'name' in attendee and attendee['name'] else "N/A"
        event_title_val = attendee['event_title'] if 'event_title' in attendee and attendee['event_title'] else "N/A"
        event_date_val = attendee['event_date'] if 'event_date' in attendee and attendee['event_date'] else "N/A"
        event_location_val = attendee['event_location'] if 'event_location' in attendee and attendee['event_location'] else "N/A"

        content = content.replace("{name}", name_val)
        content = content.replace("{event_title}", event_title_val)
        content = content.replace("{event_date}", event_date_val)
        content = content.replace("{event_location}", event_location_val)

        with open("output_{}.txt".format(attendee_number), "w") as f:
            f.write(content)
