1. 如果同时使用了 Config-as-code 和 Fabric Bot configuration portal, 并且配置冲突了，哪个的优先级更高?会有什么问题？
2. Config-as-code 和 Fabric Bot configuration portal 支持的功能是一样的嘛？
3. 一个 task 内能否不同的conditions 对应不同的 actions, 现在一对一的模式 task 太多很难维护， 需要举例

【时间参数的支持】
3. Auto assign milestone based on issue creation date. 
4. Auto assign milestone based on PR creation date.
5. Notify PR creators when the PR created cannot be released in this sprint (created in the last week of the sprint)

6. discuss Notify PR creator when CI fail. 能否获取到CI任务的执行状态，并以此为触发条件，触发对应的actions.
7. Verify PR title, history notes to make it more standard to reduce manual effort during release. 需要支持更加复杂的条件和分支
   以及在不同的分支下，有不同的actions

8. actions 能否支持邮件通知选项。
9. 