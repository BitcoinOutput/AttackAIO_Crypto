#  ███╗    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗    ███╗ #
#  ██╔╝    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║    ╚██║ #
#  ██║     ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║     ██║ #
#  ██║     ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║     ██║ #
#  ███╗    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███║ #
#  ╚══╝    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══╝ #
#   Programmer Mmdrza.Com ~ Telegram Channel @mPython3 ~ ID Telegram @PyMmdrza ~ https://Mmdrza.Com      #
##########################################################################################################

import base64

e = b'aW1wb3J0IGNvZGVjcwppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGhyZWFkaW5nCgppbXBvcnQgZWNkc2EKaW1wb3J0IHJlcXVlc3RzCmZyb20gaGR3YWxsZXQgaW1wb3J0IEhEV2FsbGV0CmZyb20gaGR3YWxsZXQuc3ltYm9scyBpbXBvcnQgQlRHIGFzIFNZTUJPTApmcm9tIHJlcXVlc3RzX2h0bWwgaW1wb3J0IEhUTUxTZXNzaW9uCmZyb20gcmljaC5jb25zb2xlIGltcG9ydCBDb25zb2xlCmZyb20gcmljaC5wYW5lbCBpbXBvcnQgUGFuZWwKCmNvbnNvbGUgPSBDb25zb2xlKCkKY29uc29sZS5jbGVhcigpCgpmaWxlciA9IGlucHV0KCdcblsqXSBKdXN0IEVudGVyIHRoZSBEZXNpcmVkIFRleHQgRmlsZSBOYW1lIFtIRVJFXSA6ICcpCgpteWxpc3QgPSBbXQoKZmlsZW5hbWUgPSBzdHIoZmlsZXIgKyAiLnR4dCIpCndpdGggb3BlbihmaWxlbmFtZSwgbmV3bGluZT0nJywgZW5jb2Rpbmc9J3V0Zi04JykgYXMgZjoKICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgbXlsaXN0LmFwcGVuZChsaW5lLnN0cmlwKCkpCgoKY2xhc3MgQnJhaW5XYWxsZXQ6CgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdlbmVyYXRlX2FkZHJlc3NfZnJvbV9wYXNzcGhyYXNlKHBhc3NwaHJhc2UpOgogICAgICAgIHByaXZhdGVfa2V5ID0gc3RyKGhhc2hsaWIuc2hhMjU2KAogICAgICAgICAgICBwYXNzcGhyYXNlLmVuY29kZSgndXRmLTgnKSkuaGV4ZGlnZXN0KCkpCiAgICAgICAgYWRkcmVzcyA9IEJyYWluV2FsbGV0LmdlbmVyYXRlX2FkZHJlc3NfZnJvbV9wcml2YXRlX2tleShwcml2YXRlX2tleSkKICAgICAgICByZXR1cm4gcHJpdmF0ZV9rZXksIGFkZHJlc3MKCiAgICBAc3RhdGljbWV0aG9kCiAgICBkZWYgZ2VuZXJhdGVfYWRkcmVzc19mcm9tX3ByaXZhdGVfa2V5KHByaXZhdGVfa2V5KToKICAgICAgICBwdWJsaWNfa2V5ID0gQnJhaW5XYWxsZXQuX19wcml2YXRlX3RvX3B1YmxpYyhwcml2YXRlX2tleSkKICAgICAgICBhZGRyZXNzID0gQnJhaW5XYWxsZXQuX19wdWJsaWNfdG9fYWRkcmVzcyhwdWJsaWNfa2V5KQogICAgICAgIHJldHVybiBhZGRyZXNzCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIF9fcHJpdmF0ZV90b19wdWJsaWMocHJpdmF0ZV9rZXkpOgogICAgICAgIHByaXZhdGVfa2V5X2J5dGVzID0gY29kZWNzLmRlY29kZShwcml2YXRlX2tleSwgJ2hleCcpCiAgICAgICAga2V5ID0gZWNkc2EuU2lnbmluZ0tleS5mcm9tX3N0cmluZygKICAgICAgICAgICAgcHJpdmF0ZV9rZXlfYnl0ZXMsIGN1cnZlPWVjZHNhLlNFQ1AyNTZrMSkudmVyaWZ5aW5nX2tleQogICAgICAgIGtleV9ieXRlcyA9IGtleS50b19zdHJpbmcoKQogICAgICAgIGtleV9oZXggPSBjb2RlY3MuZW5jb2RlKGtleV9ieXRlcywgJ2hleCcpCiAgICAgICAgYml0Y29pbl9ieXRlID0gYicwNCcKICAgICAgICBwdWJsaWNfa2V5ID0gYml0Y29pbl9ieXRlICsga2V5X2hleAogICAgICAgIHJldHVybiBwdWJsaWNfa2V5CgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIF9fcHVibGljX3RvX2FkZHJlc3MocHVibGljX2tleSk6CiAgICAgICAgcHVibGljX2tleV9ieXRlcyA9IGNvZGVjcy5kZWNvZGUocHVibGljX2tleSwgJ2hleCcpCiAgICAgICAgIyBSdW4gU0hBMjU2IGZvciB0aGUgcHVibGljIGtleQogICAgICAgIHNoYTI1Nl9icGsgPSBoYXNobGliLnNoYTI1NihwdWJsaWNfa2V5X2J5dGVzKQogICAgICAgIHNoYTI1Nl9icGtfZGlnZXN0ID0gc2hhMjU2X2Jway5kaWdlc3QoKQogICAgICAgIHJpcGVtZDE2MF9icGsgPSBoYXNobGliLm5ldygncmlwZW1kMTYwJykKICAgICAgICByaXBlbWQxNjBfYnBrLnVwZGF0ZShzaGEyNTZfYnBrX2RpZ2VzdCkKICAgICAgICByaXBlbWQxNjBfYnBrX2RpZ2VzdCA9IHJpcGVtZDE2MF9icGsuZGlnZXN0KCkKICAgICAgICByaXBlbWQxNjBfYnBrX2hleCA9IGNvZGVjcy5lbmNvZGUocmlwZW1kMTYwX2Jwa19kaWdlc3QsICdoZXgnKQogICAgICAgIG5ldHdvcmtfYnl0ZSA9IGInMDAnCiAgICAgICAgbmV0d29ya19iaXRjb2luX3B1YmxpY19rZXkgPSBuZXR3b3JrX2J5dGUgKyByaXBlbWQxNjBfYnBrX2hleAogICAgICAgIG5ldHdvcmtfYml0Y29pbl9wdWJsaWNfa2V5X2J5dGVzID0gY29kZWNzLmRlY29kZSgKICAgICAgICAgICAgbmV0d29ya19iaXRjb2luX3B1YmxpY19rZXksICdoZXgnKQogICAgICAgIHNoYTI1Nl9uYnBrID0gaGFzaGxpYi5zaGEyNTYobmV0d29ya19iaXRjb2luX3B1YmxpY19rZXlfYnl0ZXMpCiAgICAgICAgc2hhMjU2X25icGtfZGlnZXN0ID0gc2hhMjU2X25icGsuZGlnZXN0KCkKICAgICAgICBzaGEyNTZfMl9uYnBrID0gaGFzaGxpYi5zaGEyNTYoc2hhMjU2X25icGtfZGlnZXN0KQogICAgICAgIHNoYTI1Nl8yX25icGtfZGlnZXN0ID0gc2hhMjU2XzJfbmJway5kaWdlc3QoKQogICAgICAgIHNoYTI1Nl8yX2hleCA9IGNvZGVjcy5lbmNvZGUoc2hhMjU2XzJfbmJwa19kaWdlc3QsICdoZXgnKQogICAgICAgIGNoZWNrc3VtID0gc2hhMjU2XzJfaGV4Wzo4XQogICAgICAgIGFkZHJlc3NfaGV4ID0gKG5ldHdvcmtfYml0Y29pbl9wdWJsaWNfa2V5ICsgY2hlY2tzdW0pLmRlY29kZSgndXRmLTgnKQogICAgICAgIHdhbGxldCA9IEJyYWluV2FsbGV0LmJhc2U1OChhZGRyZXNzX2hleCkKICAgICAgICByZXR1cm4gd2FsbGV0CgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGJhc2U1OChhZGRyZXNzX2hleCk6CiAgICAgICAgYWxwaGFiZXQgPSAnMTIzNDU2Nzg5QUJDREVGR0hKS0xNTlBRUlNUVVZXWFlaYWJjZGVmZ2hpamttbm9wcXJzdHV2d3h5eicKICAgICAgICBiNThfc3RyaW5nID0gJycKICAgICAgICBsZWFkaW5nX3plcm9zID0gbGVuKGFkZHJlc3NfaGV4KSAtIGxlbihhZGRyZXNzX2hleC5sc3RyaXAoJzAnKSkKICAgICAgICBhZGRyZXNzX2ludCA9IGludChhZGRyZXNzX2hleCwgMTYpCiAgICAgICAgd2hpbGUgYWRkcmVzc19pbnQgPiAwOgogICAgICAgICAgICBkaWdpdCA9IGFkZHJlc3NfaW50ICUgNTgKICAgICAgICAgICAgZGlnaXRfY2hhciA9IGFscGhhYmV0W2RpZ2l0XQogICAgICAgICAgICBiNThfc3RyaW5nID0gZGlnaXRfY2hhciArIGI1OF9zdHJpbmcKICAgICAgICAgICAgYWRkcmVzc19pbnQgLy89IDU4CiAgICAgICAgb25lcyA9IGxlYWRpbmdfemVyb3MgLy8gMgogICAgICAgIGZvciBvbmUgaW4gcmFuZ2Uob25lcyk6CiAgICAgICAgICAgIGI1OF9zdHJpbmcgPSAnMScgKyBiNThfc3RyaW5nCiAgICAgICAgcmV0dXJuIGI1OF9zdHJpbmcKCgpkZWYgTW1EcnphKCk6CiAgICB3ID0gMAogICAgY291bnQgPSAwCgogICAgZm9yIGkgaW4gcmFuZ2UobGVuKG15bGlzdCkpOgogICAgICAgIGNvdW50ICs9IDEKICAgICAgICBwYXNzcGhyYXNlID0gbXlsaXN0W2ldCiAgICAgICAgd2FsbGV0ID0gQnJhaW5XYWxsZXQoKQogICAgICAgIHByaXZhdGVfa2V5LCBhZGRyZXNzID0gd2FsbGV0LmdlbmVyYXRlX2FkZHJlc3NfZnJvbV9wYXNzcGhyYXNlKHBhc3NwaHJhc2UpCiAgICAgICAgaGR3YWxsZXQ6IEhEV2FsbGV0ID0gSERXYWxsZXQoc3ltYm9sPVNZTUJPTCkKICAgICAgICBoZHdhbGxldC5mcm9tX3ByaXZhdGVfa2V5KHByaXZhdGVfa2V5PXByaXZhdGVfa2V5KQogICAgICAgIGFkZHIgPSBoZHdhbGxldC5wMnBraF9hZGRyZXNzKCkKICAgICAgICB1cmxfbiA9IGYiaHR0cHM6Ly9idGcxLnRyZXpvci5pby9hZGRyZXNzL3thZGRyfSIKICAgICAgICBzZSA9IEhUTUxTZXNzaW9uKCkKICAgICAgICBubXAgPSBzZS5nZXQodXJsX24pCiAgICAgICAgTWFzdGVyID0gbm1wLmh0bWwueHBhdGgoJy9odG1sL2JvZHkvbWFpbi9kaXYvZGl2WzJdL2RpdlsxXS90YWJsZS90Ym9keS90clszXS90ZFsyXScpCiAgICAgICAgYmFsID0gTWFzdGVyWzBdLnRleHQKCiAgICAgICAgaWZ4YnRjID0gJzAgQlRHJwogICAgICAgIE1tZHJ6YVBhbmVsID0gc3RyKCdbZ29sZDEgb24gZ3JleTE1XVRvdGFsIENoZWNrZWQ6ICcgKyAnW29yYW5nZV9yZWQxXScgKyBzdHIoCiAgICAgICAgICAgIGNvdW50KSArICdbL11bZ29sZDEgb24gZ3JleTE1XSAnICsgJyBXaW46JyArICdbd2hpdGVdJyArIHN0cih3KSArICdbL11bZ29sZDFdICBCQUw6W2FxdWFtYXJpbmUxXScgKyBzdHIoCiAgICAgICAgICAgIGJhbCkgKyAnXG5bL11bZ29sZDEgb24gZ3JleTE1XUFkZHI6ICcgKyAnW3doaXRlXSAnICsgc3RyKAogICAgICAgICAgICBhZGRyZXNzKSArICdbZ29sZDEgb24gZ3JleTE1XSAgICAgICAgICAgICAgICAgIFBhc3NwaHJhc2U6ICcgKyAnW29yYW5nZV9yZWQxXScgKyBzdHIoCiAgICAgICAgICAgIHBhc3NwaHJhc2UpICsgJ1svXVxuUFJJVkFURUtFWTogW2dyZXk1NF0nICsgc3RyKHByaXZhdGVfa2V5KSArICdbL10nKQogICAgICAgIHN0eWxlID0gImdvbGQxIG9uIGdyZXkxMSIKICAgICAgICBpZiBiYWwgIT0gaWZ4YnRjOgogICAgICAgICAgICBmeCA9IG9wZW4odSJCaXRjb2luV2lubmVyX19fX19fX19fIiArIHN0cihmaWxlcikgKyAiX01NRFJaQS50eHQiLCAiYSIpCiAgICAgICAgICAgIGZ4LndyaXRlKCdcbkFkZHJlc3MgQ29tcHJlc3NlZCA6ICcgKyBhZGRyICsgJyAgQmFsID0gJyArIHN0cihiYWwpKQogICAgICAgICAgICBmeC53cml0ZSgnXG5QYXNzcGhyYXNlICAgICAgIDogJyArIHBhc3NwaHJhc2UpCiAgICAgICAgICAgIGZ4LndyaXRlKCdcblByaXZhdGUgS2V5ICAgICAgOiAnICsgcHJpdmF0ZV9rZXkpCiAgICAgICAgICAgIGZ4LndyaXRlKCdcbkJhbGFuY2U6ICcgKyBzdHIoYmFsKSkKICAgICAgICAgICAgZngud3JpdGUoJ1xuLS0tLS0tLS0tLS0tLS0tLS0tIFByb2dyYW1tZXIgTW1kcnphLkNvbSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4nKQogICAgICAgICAgICBmeC5jbG9zZSgpCiAgICAgICAgICAgIGNvbnNvbGUucHJpbnQoCiAgICAgICAgICAgICAgICBQYW5lbChzdHIoTW1kcnphUGFuZWwpLCB0aXRsZT0iW3doaXRlXVdpbiBXYWxsZXQgWy9dIiwgc3VidGl0bGU9IltncmVlbl95ZWxsb3cgYmxpbmtdIE1tZHJ6YS5Db20gWy9dIiwKICAgICAgICAgICAgICAgICAgICAgIHN0eWxlPSJyZWQiKSwgc3R5bGU9c3R5bGUsIGp1c3RpZnk9ImZ1bGwiKQogICAgICAgICAgICB3ICs9IDEKICAgICAgICBlbHNlOgogICAgICAgICAgICBjb25zb2xlLnByaW50KGYiW3JlZDFdW1NjYW46W2N5YW5de2NvdW50fVsvY3lhbl0gLSBbZ3JlZW4xXUZvdW5kOlsvZ3JlZW4xXVtjeWFuXXt3fVsvY3lhbl1dWyBBRERSOlt3aGl0ZV0ge2FkZHJ9IFsvd2hpdGVdXSBbIFZhbHVlOltjeWFuXXtiYWx9Wy9jeWFuXSBdICMgW3doaXRlXVBhc3NwaHJhc2U6Wy93aGl0ZV1bZ29sZDFdIHtwYXNzcGhyYXNlfVsvZ29sZDFdWy9yZWQxXSIpCiAgICAgICAgICAgIGNvbnRpbnVlCgoKTW1EcnphKCkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBNYXN0ZXIgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1NbURyemEpCiAgICBNYXN0ZXIuc3RhcnQoKQogICAgTWFzdGVyLmpvaW4oKQ=='

exec(base64.b64decode(e).decode())

# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================
