\ Model Marketing Budget Optimization
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.16 channels[Print] + 0.09 channels[TV] + 0.06 channels[SEO]
   + 0.14 channels[SocialM]
Subject To
 Total_Budget: channels[Print] + channels[TV] + channels[SEO]
   + channels[SocialM] <= 1e+06
 Conv_Budget: channels[Print] + channels[TV] >= 400000
 Print_Min: channels[Print] <= 100000
 SocialM_Vs_SEO: - 3 channels[SEO] + channels[SocialM] <= 0
 Viewers_Target: 2.1 channels[Print] + 2.5 channels[TV] + 3 channels[SEO]
   + 0.9 channels[SocialM] >= 1.5e+06
Bounds
End
