import resend
import os 


resend.api_key = os.getenv("RESEND_API_KEY")

def send_reset_email(user, reset_url):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": user.email,
        "subject": "Recuperação de senha",
          "html": f"""
            <h2>Recupere sua senha</h2>
            <p>Clique no link para redefinir sua senha:</p>
            <a href="{reset_url}">Reset Password</a>
        """
    })