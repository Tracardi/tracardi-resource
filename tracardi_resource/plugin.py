from tracardi.service.storage.driver import storage
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result


class ReadResourceAction(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload):
        resource = await storage.driver.resource.load(self.event.source.id)
        return Result(port="payload", value=resource.dict())


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_resource.plugin',
            className='ReadResourceAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Risto Kowaczewski",
            init={}
        ),
        metadata=MetaData(
            name='Resource reader',
            desc='This plugin reads the source the workflow was executed from.',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )