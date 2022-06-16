const fs = require('fs')
var html = fs.readFileSync('./index.html', 'utf8' , (err, html) => {
  if (err) {
    console.error(err)
    return
  }
  return html
})
//console.log(html)
const { EmailClient } = require("@azure/communication-email");
const connectionString = "$connectionString";
const client = new EmailClient(connectionString);
const sender = "DoNotReply@688f5f34-2659-4a61-a4aa-31324494c6ef.azurecomm.net";
var emailContent = {
  subject: "Test results of Azure CLI",
  plainText: "This email is send by Azure CLI BOT\n\n Please don't reply. \\n",
  html: html,
};
//console.log(emailContent)
const toRecipients = {
  to: [
    { email: "zelinwang@microsoft.com", displayName: "ZelinWang" },
  ],
};

async function main() {
  try {
    const emailMessage = {
      sender: sender,
      content: emailContent,
      recipients: toRecipients,
    };

    const sendResult = await client.send(emailMessage);

    if (sendResult && sendResult.messageId) {
      // check mail status, wait for 5 seconds, check for 60 seconds.
      const messageId = sendResult.messageId;
      if (messageId === null) {
        console.log("Message Id not found.");
        return;
      }

      console.log("Send email success, MessageId :", sendResult.messageId);

      let counter = 0;
      const statusInterval = setInterval(async function () {
        counter++;
        try {
          const response = await client.getSendStatus(messageId);
          if (response) {
            console.log(`Email status for {${messageId}} : [${response.status}]`);
            if (response.status.toLowerCase() !== "queued" || counter > 12) {
              clearInterval(statusInterval);
            }
          }
        } catch (e) {
          console.log("Error in checking send mail status: ",e);
        }
      }, 5000);
    } else {
      console.error("Something went wrong when trying to send this email: ", sendResult);
    }
  } catch (e) {
    console.log("################### Exception occoured while sending email #####################", e);
  }
}

main();