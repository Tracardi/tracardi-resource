from tracardi.service.storage.driver import storage
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData, Documentation, PortDoc
from tracardi_plugin_sdk.domain.result import Result


class ReadResourceAction(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload):
        resource = await storage.driver.resource.load(self.event.source.id)
        return Result(port="payload", value=resource.dict(exclude={"credentials": ...}))


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_resource.plugin',
            className='ReadResourceAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.6.0.1',
            license="MIT",
            author="Risto Kowaczewski",
            init={}
        ),
        metadata=MetaData(
            name='Read resource',
            desc='This plugin reads the source that the event came from.',
            type='flowNode',
            width=200,
            height=100,
            icon='tower',
            group=["Operations"],
            documentation=Documentation(
                inputs={
                    "payload": PortDoc(desc="Reads payload object.")
                },
                outputs={
                    "payload": PortDoc(desc="Returns resource without credentials."),
                }
            ),
        )
    )