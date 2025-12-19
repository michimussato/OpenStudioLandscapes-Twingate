import textwrap

import snakemd


def readme_feature(doc: snakemd.Document) -> snakemd.Document:

    # Some Specific information

    doc.add_heading(
        text="Official Resources",
        level=1,
    )

    # Logo

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """\
                Logo Twingate\
                """
            ),
            image="https://help.twingate.com/hc/theming_assets/01HZKY9WB60MKN9FS7R4KP0J80.png",
            link="https://www.twingate.com/",
        ).__str__()
    )

    doc.add_heading(
        text="Twingate Connector",
        level=2,
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            Twingate Information:\
            """
        )
    )

    doc.add_unordered_list(
        [
            "[Github](https://github.com/Twingate-Labs)",
            "[Twingate on Docker Hub](https://hub.docker.com/u/twingate)",
            "[Twingate Connector (Docker Hub)](https://hub.docker.com/r/twingate/connector)",
            "[How to deploy a Connector](https://www.twingate.com/docs/quick-start#deploy-a-connector)",
            "[Documentation](https://www.twingate.com/docs/)",
            "[Twingate API](https://www.twingate.com/docs/api-overview)",
            "[Deploy Docker Compose](https://www.twingate.com/docs/deploy-connector-with-docker-compose)",
            "[Documentation](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/)",
            "[Tutorial/Overview (Network Chuck)](https://www.youtube.com/watch?v=IYmXPF3XUwo&ab_channel=NetworkChuck)",
        ]
    )

    doc.add_heading(
        text="Twingate Connector Setup",
        level=3,
    )

    doc.add_heading(
        text="Sign Up",
        level=4,
    )

    doc.add_unordered_list(
        [
            "[https://auth.twingate.com/signup-v2](https://auth.twingate.com/signup-v2)",
        ]
    )

    doc.add_heading(
        text="Add Remote Network",
        level=4,
    )

    doc.add_unordered_list(
        [
            "[https://openstudiolandscapes.twingate.com/networks](https://openstudiolandscapes.twingate.com/networks)",
        ]
    )

    doc.add_ordered_list(
        [
            "On Premise",
            "Set Remote Network name",
            "Add Remote Network name to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_NETWORK`)",
        ]
    )

    doc.add_heading(
        text="Add Connector",
        level=4,
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            For redundancy, Twingate sets up two Connectors. We'll
            continue with one for now.\
            """
        )
    )

    doc.add_unordered_list(
        [
            "[https://openstudiolandscapes.twingate.com/connectors](https://openstudiolandscapes.twingate.com/connectors)",
        ]
    )

    doc.add_ordered_list(
        [
            "Docker",
            "Generate New Tokens",
            "Add Access Token to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN`)",
            "Add Refresh Token to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN`)",
        ]
    )

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """\
                Not yet connected\
                """
            ),
            image="media/images/not_yet_connected.png",
        ).__str__()
    )

    doc.add_heading(
        text="Create and Launch Landscape (OpenStudioLandscapes-Twingate)",
        level=4,
    )

    doc.add_code(
        code=textwrap.dedent(
            text="""\
            [...]
            twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Offline
            twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Authentication
            twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Authentication
            twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Online
            [...]\
"""
        ),
        lang="generic",
    )

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """\
                Connected\
                """
            ),
            image="media/images/connected.png",
        ).__str__()
    )

    return doc


if __name__ == "__main__":
    pass
