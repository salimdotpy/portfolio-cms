from flask import render_template
from models import GeneralSetting, Transaction, User, Admin, UserWallet, AdminNotification, db
from helper import to_dict

class ForgotPasswordController():
    def showLinkRequestForm():
        pageTitle = 'Account Recovery'
        return view('admin.auth.passwords.email', compact('pageTitle'))

    def sendResetCodeEmail():
        user = Admin::where('email', $request->email)->first();
        if (!$user) {
            return back()->withErrors(['Email Not Available']);
        }

        code = verificationCode(6);
        $adminPasswordReset = new AdminPasswordReset();
        $adminPasswordReset->email = $user->email;
        $adminPasswordReset->token = $code;
        $adminPasswordReset->status = 0;
        $adminPasswordReset->created_at = date("Y-m-d h:i:s");
        $adminPasswordReset->save();

        $userIpInfo = getIpInfo();
        $userBrowser = osBrowser();
        sendEmail($user, 'PASS_RESET_CODE', [
            'code' => $code,
            'operating_system' => $userBrowser['os_platform'],
            'browser' => $userBrowser['browser'],
            'ip' => $userIpInfo['ip'],
            'time' => $userIpInfo['time']
        ]);

        $pageTitle = 'Account Recovery';
        $notify[] = ['success', 'Password reset email sent successfully'];
        return view('admin.auth.passwords.code_verify', compact('pageTitle', 'notify'));
    }

    public function verifyCode(Request $request)
    {
        $request->validate(['code' => 'required']);
        $notify[] = ['success', 'You can change your password.'];
        $code = str_replace(' ', '', $request->code);
        return redirect()->route('admin.password.reset.form', $code)->withNotify($notify);
    }
}
