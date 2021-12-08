with self.assertRaisesRegex(HttpResponseError,
                            'You are adding a destination that is already defined in rule: clitest. Destination must be unique across export rules in your workspace . See http://aka.ms/LADataExport#limitations'):
    pass